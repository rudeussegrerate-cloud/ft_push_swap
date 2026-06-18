import random


def gen_player_achievements() -> list:
    achievement = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
                    'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    return list(random.sample(achievement, k = random.randint(1, random.randint(5, 12))))

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    Bob = set(gen_player_achievements())
    james = set(gen_player_achievements())
    roberto = set(gen_player_achievements())
    jeremi = set(gen_player_achievements())


    Players = [Bob, james, roberto, jeremi]
    name = ('Bob', 'James', 'Roberto', 'Jeremi')
    i = 0
    for Player in Players:
        print(name[i], Player)
        i += 1

    print("\nAll distinct achievements: ", end="")
    print(Bob.union(james, jeremi, roberto))
    print(f"\nCommon achievements: {Bob.intersection(james, roberto, jeremi)}")
    
    print(f"\nOnly {name[0]} has: {Bob.difference(james, roberto, jeremi)}")
    print("Only ", name[1], "has: ", james.difference(Bob, roberto, jeremi))
    print("Only ", name[2], "has: ", roberto.difference(Bob, james, jeremi))
    print("Only ", name[3], "has: ", jeremi.difference(Bob, roberto, james))
    
    print(f"\n{name[0]} is missing: {james.union(jeremi, roberto).difference(Bob)}")
    print(f"{name[1]} is missing: {Bob.union(jeremi, roberto).difference(james)}")
    print(f"{name[2]} is missing: {james.union(Bob, roberto).difference(jeremi)}")
    print(f"{name[3]} is missing: {james.union(jeremi, Bob).difference(roberto)}")
