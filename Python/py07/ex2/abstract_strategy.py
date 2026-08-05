from abc import ABC, abstractmethod
from ex0.creature_type import Creature
from ex1.concret_capacity import Sproutling, Bloomelle
from ex1.transformf_actory import Shiftling, Morphagon


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.name = None


    @abstractmethod
    def act(self, creatur: Creature) -> None:
        pass


    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Normal"

    def act(self, creatur: Creature) -> None:
        return creatur.attack()


    def is_valid(self) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Aggressive"

    def act(self, creatur: Shiftling | Morphagon):
        if self.is_valid(creatur):
            creatur.transform()
            creatur.attack()
            creatur.revert()
        else:
            raise Exception("Error, this creature isn't compatible with this strategy!")


    def is_valid(self, creatur: Shiftling | Morphagon) -> bool:
        if isinstance(creatur, Shiftling | Morphagon):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Defensive"


    def act(self, creatur: Sproutling | Bloomelle):
        if self.is_valid(creatur):
            creatur.attack()
            creatur.heal()
        else:
            raise Exception("Error, this creature isn't compatible with this strategy!")


    def is_valid(self, creatur: Sproutling | Bloomelle) -> bool:
        return isinstance(creatur, Sproutling | Bloomelle)
