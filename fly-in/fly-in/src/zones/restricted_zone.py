from .zone import Zone


class RestrictedZone(Zone):
    """ Class pour la zone restrainte"""
    def __init__(self,
                 name: str,
                 coord: tuple[int, int],
                 max_drones: int = 1,
                 color: str | None = None) -> None:
        """initialisation des element du zone"""
        super().__init__(name, coord, max_drones, color)

    def get_movement_cost(self) -> float:
        """retoune le cout pour atteindre cette zone."""
        return 2
