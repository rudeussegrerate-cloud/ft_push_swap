"""Graph model: zones + connections without any graph library."""

from typing import Optional
from utile.zone import Zone
from utile.connection import Connection


class Graph:
    """Routing graph made of zones (nodes) and connections (edges).

    No external graph libraries (networkx, graphlib, etc.) are used.
    Adjacency is computed on the fly from the connections list.
    """

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.zones: dict[str, Zone] = {}
        self.connections: list[Connection] = []

    # ------------------------------------------------------------------ zones

    def add_zone(self, zone: Zone) -> None:
        """Add a zone to the graph.

        Args:
            zone: Zone instance to add.
        """
        self.zones[zone.name] = zone

    def get_zone(self, name: str) -> Optional[Zone]:
        """Return the zone with the given name, or None.

        Args:
            name: Zone name to look up.

        Returns:
            The Zone, or None if not found.
        """
        return self.zones.get(name)

    def start_zone(self) -> Optional[Zone]:
        """Return the unique start zone, or None.

        Returns:
            The Zone marked as start, or None.
        """
        for zone in self.zones.values():
            if zone.is_start:
                return zone
        return None

    def end_zone(self) -> Optional[Zone]:
        """Return the unique end zone, or None.

        Returns:
            The Zone marked as end, or None.
        """
        for zone in self.zones.values():
            if zone.is_end:
                return zone
        return None

    # --------------------------------------------------------------- connections

    def add_connection(self, connection: Connection) -> None:
        """Add a connection to the graph.

        Args:
            connection: Connection instance to add.
        """
        self.connections.append(connection)

    def get_connection(self, zone1: str, zone2: str) -> Optional[Connection]:
        """Return the connection between two zones, or None.

        Args:
            zone1: First zone name.
            zone2: Second zone name.

        Returns:
            The Connection, or None if they are not directly connected.
        """
        for conn in self.connections:
            if conn.connects(zone1) and conn.connects(zone2):
                return conn
        return None

    # --------------------------------------------------------------- traversal

    def get_neighbors(self, zone_name: str) -> list[Zone]:
        """Return accessible neighbor zones of the given zone.

        Blocked zones are excluded from the result.

        Args:
            zone_name: Name of the zone whose neighbors are requested.

        Returns:
            List of accessible neighbor Zone instances.
        """
        neighbors: list[Zone] = []
        for conn in self.connections:
            if conn.connects(zone_name):
                neighbor_name = conn.other(zone_name)
                zone = self.zones.get(neighbor_name)
                if zone is not None and zone.is_accessible():
                    neighbors.append(zone)
        return neighbors

    def get_neighbor_connections(
        self, zone_name: str
    ) -> list[tuple[Zone, Connection]]:
        """Return (neighbor_zone, connection) pairs for accessible neighbors.

        Args:
            zone_name: Name of the zone to query.

        Returns:
            List of (Zone, Connection) tuples for each accessible neighbor.
        """
        result: list[tuple[Zone, Connection]] = []
        for conn in self.connections:
            if conn.connects(zone_name):
                neighbor_name = conn.other(zone_name)
                zone = self.zones.get(neighbor_name)
                if zone is not None and zone.is_accessible():
                    result.append((zone, conn))
        return result

    def __repr__(self) -> str:
        """Return a summary of the graph."""
        return (
            f"Graph({len(self.zones)} zones, "
            f"{len(self.connections)} connections)"
        )
