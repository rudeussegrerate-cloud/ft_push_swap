from ex0.creature_creation import FlameFactory, AquaFactory
from ex1.concret_capacity import HealingCreatureFactory
from ex1.transformf_actory import TransformCreatureFactory
from ex0.creature_creation import CreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.abstract_strategy import BattleStrategy, StrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures_with_strategies = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        creatures_with_strategies.append((creature, strategy))
    for i in range(len(creatures_with_strategies)):
        for j in range(i + 1, len(creatures_with_strategies)):
            c1, s1 = creatures_with_strategies[i]
            c2, s2 = creatures_with_strategies[j]

            print("\n* Battle *")
            print(f"{c1.describe()}\nvs.\n{c2.describe()}\nnow fight!")

            try:
                print(s1.act(c1))
                print(s2.act(c2))
            except (StrategyError) as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        healing_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()

        normal = NormalStrategy()
        aggressive = AggressiveStrategy()
        defensive = DefensiveStrategy()
        try:
            print("Tournament 0 (basic)")
            tournament_0: list[tuple[CreatureFactory, BattleStrategy]] = [
                (flame_factory, normal),
                (aqua_factory, normal)
            ]
            names = [f"({type(f).__name__}+{type(s).__name__})"
                     for f, s in tournament_0]
            print(f"[ {', '.join(names)} ]")
            battle(tournament_0)
        except (Exception, StrategyError) as e:
            print(e)

        print("\n" + "="*40 + "\n")

        print("Tournament 1 (error)")
        try:
            tournament_1: list[tuple[CreatureFactory, BattleStrategy]] = [
                (flame_factory, defensive),
                (healing_factory, aggressive)
            ]
            names = [f"({type(f).__name__}+{type(s).__name__})"
                     for f, s in tournament_1]
            print(f"[ {', '.join(names)} ]")
            battle(tournament_1)
        except (Exception, StrategyError) as e:
            print(e)

        print("\n" + "="*40 + "\n")

        print("Tournament 2 (multiple)")
        try:
            tournament_2: list[tuple[CreatureFactory, BattleStrategy]] = [
                (aqua_factory, normal),
                (healing_factory, defensive),
                (transform_factory, aggressive)
            ]
            names = [f"({type(f).__name__}+{type(s).__name__})"
                     for f, s in tournament_2]
            print(f"[ {', '.join(names)} ]")
            battle(tournament_2)
        except (Exception, StrategyError) as e:
            print(e)
    except (Exception, StrategyError) as e:
        print("Got Error: ", e)
