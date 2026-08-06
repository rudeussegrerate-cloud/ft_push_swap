from abc import ABC, abstractmethod
from ex0.creature_type import Creature
from ex1.concret_capacity import Sproutling, Bloomelle
from ex1.transformf_actory import Shiftling, Morphagon


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.name = None

    @abstractmethod
    def is_valid(self, creatur: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creatur: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creatur: Creature) -> str:
        if self.is_valid(creatur):
            return creatur.attack()
        else:
            raise StrategyError("Error, {creatur._name} isn't \
compatible with Normal strategy!")

    def is_valid(self, creatur: Creature) -> bool:
        return isinstance(creatur, Creature)


class AggressiveStrategy(BattleStrategy):

    def act(self, creatur: Shiftling | Morphagon) -> str:
        if self.is_valid(creatur):
            res1 = creatur.transform()
            res2 = creatur.attack()
            res3 = creatur.revert()
            return f"{res1}\n{res2}\n{res3}"
        else:
            raise StrategyError(f"Error, {creatur._name} isn't \
compatible with Aggressive strategy!")

    def is_valid(self, creatur: Shiftling | Morphagon) -> bool:
        return isinstance(creatur, Shiftling | Morphagon)


class DefensiveStrategy(BattleStrategy):
    def act(self, creatur: Sproutling | Bloomelle) -> None:
        if self.is_valid(creatur):
            res1 = creatur.attack()
            res2 = creatur.heal()
            return f"{res1}\n{res2}"
        else:
            raise StrategyError(f"Error, {creatur._name} isn't \
                                  compatible with Defensive strategy!")

    def is_valid(self, creatur: Sproutling | Bloomelle) -> bool:
        return isinstance(creatur, Sproutling | Bloomelle)
