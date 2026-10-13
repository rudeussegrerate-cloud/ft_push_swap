from abc import ABC, abstractmethod


class Zone(ABC):
    """Décrit ce qu'est une Zone en général."""

    def __init__(self, name: str,
                 coord: tuple[int, int],
                 max_drones: int = 1,
                 color: str | None = None) -> None:
        """Initialisation de la class zone, parent de tous les type de zone"""
        self.name: str = name
        self.coord: tuple[int, int] = coord
        self.max_drones: int = max_drones
        self.color: str | None = color

    @abstractmethod
    def get_movement_cost(self) -> float:
        """Pour retourner le nombre de cout pour chaque zone."""
        pass
