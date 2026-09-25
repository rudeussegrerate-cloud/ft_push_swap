from .zone import Zone


class BlockedZone(Zone):
    """ Class pour la zone Blocker"""
    def __init__(self, name: str,
                 coord: tuple[int, int],
                 max_drones: int = 1,
                 color: str | None = None) -> None:
        """initialiation."""
        super().__init__(name, coord, max_drones, color)

    def get_movement_cost(self) -> float:
        """retoune le cout pour atteindre cette zone."""
        return float("inf")
