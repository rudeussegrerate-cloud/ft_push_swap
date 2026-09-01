#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    try:
        c1 = HealingCreatureFactory()
        base_heal = c1.create_base()
        evol_heal = c1.create_evolved()

        print("Testing Creature with healing capability")
        print(" base: ")
        print(f"{base_heal.describe()}")
        print(base_heal.attack())
        print(base_heal.heal())

        print(" evolve:")
        print(evol_heal.describe())
        print(evol_heal.attack())
        print(evol_heal.heal())

        c2 = TransformCreatureFactory()
        base_transf = c2.create_base()
        evol_transf = c2.create_evolved()

        print("\nTesting Creature with transform capability")
        print("base:")
        print(f"{base_transf.describe()}")
        print(base_transf.attack())
        print(base_transf.transform())
        print(base_transf.attack())
        print(base_transf.revert())

        print(" evolved: ")
        print(evol_transf.describe())
        print(evol_transf.attack())
        print(evol_transf.transform())
        print(evol_transf.attack())
        print(evol_transf.revert())
    except Exception as e:
        print(f"Got error: {e}")
