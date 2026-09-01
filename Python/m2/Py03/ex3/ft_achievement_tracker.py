#!/usr/bin/env python3
import random
achievement = ['Crafting Genius', 'Strategist', 'World Savior',
               'Speed Runner', 'Survivor', 'Master Explorer',
               'Treasure Hunter', 'Unstoppable', 'First Steps',
               'Collector Supreme', 'Untouchable', 'Sharp Mind',
               'Boss Slayer']


def gen_player_achievements() -> set[str]:
    if not achievement:
        return set()
    return set(random.sample(achievement,
               k=random.randint(1, random.randint(5, 12))))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    bob = gen_player_achievements()
    james = gen_player_achievements()
    roberto = gen_player_achievements()
    jeremi = gen_player_achievements()

    players = [bob, james, roberto, jeremi]
    name = ('Bob', 'James', 'Roberto', 'Jeremi')
    i = 0
    for player in players:
        print(name[i], player)
        i += 1

    print("\nAll distinct achievements: ", end="")
    print(bob.union(james, jeremi, roberto))
    print(f"\nCommon achievements: {bob.intersection(james, roberto, jeremi)}")

    print(f"\nOnly {name[0]} has: {bob.difference(james, roberto, jeremi)}")
    print("Only ", name[1], "has: ", james.difference(bob, roberto, jeremi))
    print("Only ", name[2], "has: ", roberto.difference(bob, james, jeremi))
    print("Only ", name[3], "has: ", jeremi.difference(bob, roberto, james))

    print(f"\n{name[0]} is missing: ", end="")
    print(f"{set(achievement) - (bob)}")
    print(f"{name[1]} is missing: ", end="")
    print(f"{set(achievement) - (james)}")
    print(f"{name[2]} is missing: ", end="")
    print(f"{set(achievement) - (roberto)}")
    print(f"{name[3]} is missing: ", end="")
    print(f"{set(achievement) - (jeremi)}")
