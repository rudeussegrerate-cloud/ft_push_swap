"""Connection model representing edges between zones."""


class Connection:
    """A bidirectional edge between two zones in the routing graph.

    Args:
        zone1: Name of the first zone.
        zone2: Name of the second zone.
        max_link_capacity: Max drones traversing simultaneously (default: 1).
    """

    def __init__(
        self,
        zone1: str,
        zone2: str,
        max_link_capacity: int = 1,
    ) -> None:
        """Initialize a Connection."""
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity

    def connects(self, zone_name: str) -> bool:
        """Return True if this connection involves the given zone.

        Args:
            zone_name: Zone name to check.

        Returns:
            True if zone_name is either endpoint of this connection.
        """
        return zone_name in (self.zone1, self.zone2)

    def other(self, zone_name: str) -> str:
        """Return the name of the zone on the other end of this connection.

        Args:
            zone_name: One endpoint zone name.

        Returns:
            The other endpoint zone name.
        """
        if zone_name == self.zone1:
            return self.zone2
        return self.zone1

    def key(self) -> tuple[str, str]:
        """Return a canonical (sorted) key for duplicate detection.

        Returns:
            Tuple with zone names in sorted order.
        """
        return (min(self.zone1, self.zone2), max(self.zone1, self.zone2))

    def __repr__(self) -> str:
        """Return a string representation of the connection."""
        return (
            f"Connection({self.zone1}-{self.zone2}, "
            f"cap={self.max_link_capacity})"
        )
