#!/usr/bin/env python3
import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    m_layer = ['martin', 'Bernard', 'thomas', 'Robert', 'lopez',
               'Guillot', 'Berger', 'gerrard']
    try:
        init_liste = random.sample(m_layer, k=random.randint(3, 7))
        new_liste = [new.capitalize() for new in init_liste]
        print(f"Initial list of players: {init_liste}")
        print(f"New list with all names capitalized: {new_liste}")
        capital_only = [cap for cap in init_liste if cap == cap.capitalize()]
        print(f"New list of capitalized names only: {capital_only}")
        score = {player: random.randint(0, 1000) for player in init_liste}
        print(f"Score dict: {score}")
        average = round(sum(score.values())/len(score), 2)
        print(f"Score average is {average}")
        best_score = {high: score[high] for high in score
                      if score[high] > average}
        print(f"High scores: {best_score}")
    except Exception as e:
        print(f"Error : {e}")
