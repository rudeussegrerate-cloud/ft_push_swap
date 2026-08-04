from ex0.creature_type import Creature
from ex0.creature_creation import CreatureFactory
from ex1 import capacity


class Sproutling(Creature):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)


    def attack(self) -> str:
        return f"{self._name} use  Vine Whip!"


    def heal(self) -> str:
        return f"{self._name} heals itself and others for a small amount"


class Bloomelle(Creature, capacity.HealCapability):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)


    def attack(self) -> str:
        return f"{self._name} use Petal Dance!"


    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()


    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")


    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")

