#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
from ex0.creature_type import Creature
from ex1.capacity import HealCapability, TransformCapability
from ex1.concret_capacity import Sproutling, Bloomelle
from ex1.transformf_actory import Shiftling, Morphagon


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creatur: Any) -> bool:
        pass

    @abstractmethod
    def act(self, creatur: Any) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creatur: Creature) -> str:
        if self.is_valid(creatur):
            return creatur.attack()
        else:
            raise StrategyError(f"Invalid Creature '{creatur.name}' isn't \
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
            raise StrategyError(f"Invalid Creature '{creatur.name}' isn't \
compatible with Aggressive strategy!")

    def is_valid(self, creatur: Shiftling | Morphagon) -> bool:
        return isinstance(creatur, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creatur: Sproutling | Bloomelle) -> str:
        if self.is_valid(creatur):
            res1 = creatur.attack()
            res2 = creatur.heal()
            return f"{res1}\n{res2}"
        else:
            raise StrategyError(f"Invalid Creature '{creatur.name}' isn't \
compatible with Defensive strategy!")

    def is_valid(self, creatur: Sproutling | Bloomelle) -> bool:
        return isinstance(creatur, HealCapability)
