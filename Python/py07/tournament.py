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

        print("Tournament 0 (basic)")
        print("[ (Flameling+Normal), (Healing+Defensive) ]")
        battle([
            (flame_factory, normal),
            (healing_factory, defensive)
        ])

        print("\n" + "="*40 + "\n")

        print("Tournament 1 (error)")
        print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle([
            (flame_factory, aggressive),
            (healing_factory, defensive)
            ])

        print("\n" + "="*40 + "\n")

        print("Tournament 2 (multiple)")
        print("[ (Aquabub+Normal), (Healing+Defensive), \
    (Transform+Aggressive) ]")
        battle([
            (aqua_factory, normal),
            (healing_factory, defensive),
            (transform_factory, aggressive)
        ])
    except (Exception, StrategyError) as e:
        print("Got Error: ", e)
