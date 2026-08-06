from ex0.creature_type import Creature
from ex0.creature_creation import CreatureFactory
from ex1.capacity import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        if not self._is_transform:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._is_transform = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._is_transform = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        if not self._is_transform:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._is_transform = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._is_transform = False
        return f"{self._name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
