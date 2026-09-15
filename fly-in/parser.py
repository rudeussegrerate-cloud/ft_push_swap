"""Parser for Fly-in map files (.txt format)."""

import re
from typing import Optional
from zone import Zone, ZoneType
from connection import Connection
from graph import Graph


class ParseError(Exception):
    """Raised when the map file contains a syntax or semantic error.

    Args:
        line_num: 1-based line number where the error occurred (0 = file level).
        message: Human-readable description of the problem.
    """

    def __init__(self, line_num: int, message: str) -> None:
        """Initialize ParseError."""
        super().__init__(f"Line {line_num}: {message}" if line_num else message)
        self.line_num = line_num


class MapParser:
    """Parses a Fly-in .txt map file into a (nb_drones, Graph) pair.

    Usage::

        parser = MapParser()
        nb_drones, graph = parser.parse_file("maps/easy/01_linear_path.txt")
    """

    # ---------------------------------------------------------------- public API

    def parse_file(self, filepath: str) -> tuple[int, Graph]:
        """Parse a map file and return (nb_drones, graph).

        Args:
            filepath: Path to the .txt map file.

        Returns:
            A tuple (nb_drones, Graph).

        Raises:
            ParseError: On any syntax or semantic error in the file.
        """
        try:
            with open(filepath, "r") as fh:
                lines = fh.readlines()
        except OSError as exc:
            raise ParseError(0, f"Cannot open file: {exc}") from exc
        return self._parse_lines(lines)

    # --------------------------------------------------------------- internals

    def _parse_metadata(self, bracket_str: str, line_num: int) -> dict[str, str]:
        """Parse a [key=val ...] metadata block into a dict.

        Args:
            bracket_str: The raw bracket string including [ and ].
            line_num: Line number for error reporting.

        Returns:
            Dict mapping metadata key strings to value strings.

        Raises:
            ParseError: If the block is syntactically invalid.
        """
        inner = bracket_str.strip()
        if not inner.startswith("[") or not inner.endswith("]"):
            raise ParseError(line_num, f"Malformed metadata block: {bracket_str!r}")
        inner = inner[1:-1]
        meta: dict[str, str] = {}
        for match in re.finditer(r'(\w+)=([^\s\]]+)', inner):
            meta[match.group(1)] = match.group(2)
        # Detect any garbage that didn't match
        cleaned = re.sub(r'\w+=\S+', '', inner).strip()
        if cleaned:
            raise ParseError(line_num, f"Invalid metadata content: {cleaned!r}")
        return meta

    def _parse_zone_line(
        self, prefix: str, rest: str, line_num: int
    ) -> Zone:
        """Parse a hub / start_hub / end_hub line into a Zone.

        Args:
            prefix: One of 'hub', 'start_hub', 'end_hub'.
            rest: Everything after the colon on that line.
            line_num: Line number for error reporting.

        Returns:
            A Zone instance.

        Raises:
            ParseError: On any syntax or constraint violation.
        """
        # Split off optional metadata block
        meta: dict[str, str] = {}
        meta_match = re.search(r'\[([^\]]*)\]', rest)
        if meta_match:
            meta = self._parse_metadata(f"[{meta_match.group(1)}]", line_num)
            rest = rest[: meta_match.start()].strip()

        parts = rest.strip().split()
        if len(parts) < 3:
            raise ParseError(
                line_num,
                f"Zone definition requires '<name> <x> <y>' — got: {rest!r}",
            )

        name = parts[0]
        if "-" in name or " " in name:
            raise ParseError(
                line_num,
                f"Zone name {name!r} must not contain dashes or spaces",
            )

        try:
            x, y = int(parts[1]), int(parts[2])
        except ValueError:
            raise ParseError(line_num, "Zone coordinates must be integers")

        # Zone type
        zone_type_str = meta.get("zone", "normal")
        try:
            zone_type = ZoneType(zone_type_str)
        except ValueError:
            raise ParseError(
                line_num,
                f"Invalid zone type {zone_type_str!r} — "
                "must be one of: normal, blocked, restricted, priority",
            )

        # max_drones
        max_drones_str = meta.get("max_drones", None)
        is_start = prefix == "start_hub"
        is_end = prefix == "end_hub"

        if max_drones_str is not None:
            try:
                max_drones = int(max_drones_str)
                if max_drones <= 0:
                    raise ValueError
            except ValueError:
                raise ParseError(line_num, "max_drones must be a positive integer")
        else:
            # start/end zones accept unlimited drones by default
            max_drones = 999 if (is_start or is_end) else 1

        color: Optional[str] = meta.get("color", None)

        return Zone(name, x, y, zone_type, color, max_drones, is_start, is_end)

    def _parse_connection_line(
        self,
        rest: str,
        defined_zones: set[str],
        line_num: int,
    ) -> Connection:
        """Parse a connection line into a Connection.

        Args:
            rest: Everything after 'connection:'.
            defined_zones: Set of zone names already parsed.
            line_num: Line number for error reporting.

        Returns:
            A Connection instance.

        Raises:
            ParseError: On unknown zones, bad format, or invalid capacity.
        """
        meta: dict[str, str] = {}
        meta_match = re.search(r'\[([^\]]*)\]', rest)
        if meta_match:
            meta = self._parse_metadata(f"[{meta_match.group(1)}]", line_num)
            rest = rest[: meta_match.start()].strip()

        rest = rest.strip()
        if rest.count("-") != 1:
            raise ParseError(
                line_num,
                f"Connection must be 'zone1-zone2' — got: {rest!r}",
            )

        zone1, zone2 = rest.split("-")
        zone1, zone2 = zone1.strip(), zone2.strip()

        for name in (zone1, zone2):
            if name not in defined_zones:
                raise ParseError(
                    line_num, f"Unknown zone {name!r} in connection"
                )

        cap_str = meta.get("max_link_capacity", "1")
        try:
            cap = int(cap_str)
            if cap <= 0:
                raise ValueError
        except ValueError:
            raise ParseError(line_num, "max_link_capacity must be a positive integer")

        return Connection(zone1, zone2, cap)

    def _parse_lines(self, lines: list[str]) -> tuple[int, Graph]:
        """Core parsing logic over a list of raw text lines.

        Args:
            lines: Lines of the map file (including newlines).

        Returns:
            (nb_drones, Graph) tuple.

        Raises:
            ParseError: On any error.
        """
        nb_drones: Optional[int] = None
        graph = Graph()
        start_count = 0
        end_count = 0
        seen_connections: set[tuple[str, str]] = set()

        # Validate that the first meaningful line is nb_drones
        first_meaningful: Optional[tuple[int, str]] = None
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                first_meaningful = (idx, stripped)
                break

        if first_meaningful is None:
            raise ParseError(0, "File is empty or contains only comments")

        first_line_num, first_line = first_meaningful
        if not first_line.startswith("nb_drones:"):
            raise ParseError(
                first_line_num,
                "First non-comment line must define nb_drones",
            )

        try:
            nb_drones = int(first_line.split(":")[1].strip())
            if nb_drones <= 0:
                raise ValueError
        except (ValueError, IndexError):
            raise ParseError(first_line_num, "nb_drones must be a positive integer")

        # Parse remaining lines
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            if ":" not in stripped:
                raise ParseError(line_num, f"Invalid line (missing ':'): {stripped!r}")

            colon_pos = stripped.index(":")
            key = stripped[:colon_pos].strip()
            value = stripped[colon_pos + 1:].strip()

            if key == "nb_drones":
                continue  # already handled

            elif key in ("start_hub", "end_hub", "hub"):
                zone = self._parse_zone_line(key, value, line_num)
                if zone.name in graph.zones:
                    raise ParseError(line_num, f"Duplicate zone name: {zone.name!r}")
                if zone.is_start:
                    start_count += 1
                    if start_count > 1:
                        raise ParseError(line_num, "Multiple start_hub zones defined")
                if zone.is_end:
                    end_count += 1
                    if end_count > 1:
                        raise ParseError(line_num, "Multiple end_hub zones defined")
                graph.add_zone(zone)

            elif key == "connection":
                defined_zones = set(graph.zones.keys())
                conn = self._parse_connection_line(value, defined_zones, line_num)
                ck = conn.key()
                if ck in seen_connections:
                    raise ParseError(
                        line_num,
                        f"Duplicate connection: {conn.zone1}-{conn.zone2}",
                    )
                seen_connections.add(ck)
                graph.add_connection(conn)

            else:
                raise ParseError(line_num, f"Unknown keyword: {key!r}")

        # Post-parse validation
        if start_count == 0:
            raise ParseError(0, "No start_hub defined")
        if end_count == 0:
            raise ParseError(0, "No end_hub defined")

        assert nb_drones is not None
        return nb_drones, graph
