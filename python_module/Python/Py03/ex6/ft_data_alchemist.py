import random

if __name__ == "__main__":
    # print("Last Dance 16:59")
    print("=== Game Data Alchemist ===")
    m_layer = ['martin', 'Bernard', 'thomas', 'Robert', 'lopez', 'Guillot', 'Berger', 'gerrard']
    init_liste = random.sample(m_layer, k = random.randint(3, 7))
    new_liste = [''] * len(init_liste)
    i = 0
    for capitalize in init_liste:
        if capitalize == capitalize.capitalize():
            i += 1
    c_liste = [''] * i
    j = 0
    i = 0
    dict_score = {}
    for liste in init_liste:
        new_liste[j] = liste.capitalize()
        if liste == liste.capitalize():
            c_liste[i] = liste
            i += 1 
        dict_score.update({liste : random.randint(0, 1000)})
        j += 1

    print(f"Initial list of players: {init_liste}")
    print(f"New list of capitalized names only: {c_liste}")
    print(f"Score dict: {dict_score}")
    try:
        print(f"Score average is: {round(sum(dict_score.values())/len(dict_score.values()), 1)}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Score avarage is: 0")

high_score = {}
for dict in dict_score:
    if dict_score[dict] > round(sum(dict_score.values())/len(dict_score.values()), 1):
        high_score.update({dict : dict_score[dict]})
print(f"High scores: {high_score}")

