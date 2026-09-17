"""Zone model for the Fly-in drone routing system."""

from enum import Enum
from typing import Optional


class ZoneType(str, Enum):
    """Types of zones with their movement cost semantics."""

    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class Zone:
    """Represents a node in the drone routing graph.

    Args:
        name: Unique zone identifier (no dashes or spaces).
        x: X coordinate (integer).
        y: Y coordinate (integer).
        zone_type: Zone movement type (default: NORMAL).
        color: Optional display color string.
        max_drones: Maximum drones allowed simultaneously (default: 1).
        is_start: True if this is the starting zone.
        is_end: True if this is the ending zone.
    """

    def __init__(
        self,
        name: str,
        x: int,
        y: int,
        zone_type: ZoneType = ZoneType.NORMAL,
        color: Optional[str] = None,
        max_drones: int = 1,
        is_start: bool = False,
        is_end: bool = False,
    ) -> None:
        """Initialize a Zone."""
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones
        self.is_start = is_start
        self.is_end = is_end

    def movement_cost(self) -> int:
        """Return the number of turns required to enter this zone.

        Returns:
            2 for restricted zones, 1 for all others.
        """
        if self.zone_type == ZoneType.RESTRICTED:
            return 2
        return 1

    def is_accessible(self) -> bool:
        """Return True if drones can enter this zone.

        Returns:
            False for BLOCKED zones, True otherwise.
        """
        return self.zone_type != ZoneType.BLOCKED

    def is_priority(self) -> bool:
        """Return True if this is a priority zone (preferred in pathfinding).

        Returns:
            True if zone_type is PRIORITY.
        """
        return self.zone_type == ZoneType.PRIORITY

    def __repr__(self) -> str:
        """Return a string representation of the zone."""
        return (
            f"Zone({self.name!r}, type={self.zone_type.value}, "
            f"max={self.max_drones}, start={self.is_start}, end={self.is_end})"
        )
