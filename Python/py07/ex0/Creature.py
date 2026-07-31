from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        super().__init__()
        self._name = name
        self._type = type
        
    @abstractmethod
    def attack(self) -> str:
        pass


    def describe(self) -> str:
        return f"{self._name} {self._type}"


class Flameling(Creature):

    def attack(self) -> str:
        return "feu"


class Pyrodon(Creature):
    def attack(self) -> str:
        return 


class Aquabub(Creature):
    def attack(self) -> str:
        return


class Torragon(Creature):
    def attack(self) -> str:
        return

