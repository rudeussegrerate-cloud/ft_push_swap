from ex2.abstract_strategy import BattleStrategy, AggressiveStrategy, DefensiveStrategy, NormalStrategy
from ex0 import FlameFactory, AquaFactory, creature_creation
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory


def Battle(opponent: list[tuple[creature_creation.CreatureFactory, BattleStrategy]]) -> None:
    for player in opponent:
        print(f"{player[0]._name} + {player[1].name}")


if __name__ == "__main__":
    s1 = NormalStrategy()
    s2 = AggressiveStrategy()
    s3 = DefensiveStrategy()

    op = [(FlameFactory().create_base(), s1), (HealingCreatureFactory().create_base(), s2)]
    Battle(op)
