class Drone():
    """Objet Drone"""
    def __init__(self, id: int, prime: bool = False) -> None:
        """ initialisation de l'objet drone """
        self.id: int = id
        self.name: str = f"D{id}"
        self.next: list[tuple[str, tuple[int, int]]] = [("", (0, 0))]
        self.position: list[tuple[str, tuple[int, int]]] = [("", (0, 0))]
        self.is_prime: bool = prime
