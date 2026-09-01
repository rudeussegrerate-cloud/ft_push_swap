#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory
from ex0.creature_creation import CreatureFactory


def script_verify(factory: CreatureFactory) -> None:
    print("Testing factory")
    c1 = factory.create_base()
    print(c1.describe())
    print(c1.attack())
    c2 = factory.create_evolved()
    print(c2.describe())
    print(c2.attack())
    print("")


def battle_mode(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(f"{c1.describe()}\nvs.\n {c2.describe()}")
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    try:
        creature1 = FlameFactory()
        creature2 = AquaFactory()
        script_verify(creature1)
        script_verify(creature2)
        battle_mode(creature1, creature2)
    except Exception as e:
        print(f"Got error: {e}")
