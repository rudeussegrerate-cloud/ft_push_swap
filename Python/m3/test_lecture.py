# 
import heapq
from itertools import count

# ---------- Environnement ----------

def voisins(pos, grille):
    x, y = pos
    candidats = [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # bouger ou rester
    resultat = []
    for nx, ny in candidats:
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]) and grille[nx][ny] == 0:
            resultat.append((nx, ny))
    return resultat


# ---------- A* niveau bas, respectant les contraintes ----------

def a_star(grille, depart, but, contraintes_sommet, contraintes_arete, horizon):
    """
    contraintes_sommet : set of (agent_pos, temps) interdits
    contraintes_arete  : set of (pos_avant, pos_apres, temps) interdits
    """
    compteur = count()
    depart_etat = (depart, 0)  # (position, temps)
    frontiere = [(0, next(compteur), depart_etat, [depart])]
    visites = set()

    while frontiere:
        cout, _, (pos, t), chemin = heapq.heappop(frontiere)

        if pos == but and t >= horizon:
            return chemin

        if (pos, t) in visites:
            continue
        visites.add((pos, t))

        if t > horizon:
            continue

        for npos in voisins(pos, grille):
            nt = t + 1

            if (npos, nt) in contraintes_sommet:
                continue
            if (pos, npos, nt) in contraintes_arete:
                continue

            heapq.heappush(
                frontiere,
                (cout + 1, next(compteur), (npos, nt), chemin + [npos])
            )

    return None  # aucun chemin trouvé


# ---------- Détection de conflit entre deux chemins ----------

def trouver_conflit(chemins):
    duree_max = max(len(c) for c in chemins.values())

    for t in range(duree_max):
        positions_t = {}
        for agent, chemin in chemins.items():
            pos = chemin[t] if t < len(chemin) else chemin[-1]
            positions_t[agent] = pos

        # collision de sommet
        vus = {}
        for agent, pos in positions_t.items():
            if pos in vus:
                return {"type": "sommet", "agents": (vus[pos], agent), "pos": pos, "temps": t}
            vus[pos] = agent

        # collision d'arête (échange de positions)
        if t > 0:
            for a1 in chemins:
                for a2 in chemins:
                    if a1 >= a2:
                        continue
                    pos_a1_avant = chemins[a1][t-1] if t-1 < len(chemins[a1]) else chemins[a1][-1]
                    pos_a1_maint = chemins[a1][t] if t < len(chemins[a1]) else chemins[a1][-1]
                    pos_a2_avant = chemins[a2][t-1] if t-1 < len(chemins[a2]) else chemins[a2][-1]
                    pos_a2_maint = chemins[a2][t] if t < len(chemins[a2]) else chemins[a2][-1]

                    if pos_a1_avant == pos_a2_maint and pos_a1_maint == pos_a2_avant:
                        return {"type": "arete", "agents": (a1, a2),
                                "pos_avant": pos_a1_avant, "pos_apres": pos_a1_maint, "temps": t}
    return None


# ---------- Nœud de l'arbre CBS ----------

class Noeud:
    def __init__(self, contraintes, chemins):
        self.contraintes = contraintes  # dict agent -> (set sommets, set aretes)
        self.chemins = chemins          # dict agent -> chemin
        self.cout = sum(len(c) for c in chemins.values())

    def __lt__(self, autre):
        return self.cout < autre.cout


# ---------- CBS niveau haut ----------

def cbs(grille, agents):
    """
    agents : dict {nom_agent: (depart, but)}
    """
    compteur = count()

    # nœud racine : aucune contrainte
    contraintes_init = {a: (set(), set()) for a in agents}
    chemins_init = {}
    for a, (depart, but) in agents.items():
        chemin = a_star(grille, depart, but, set(), set(), horizon=20)
        if chemin is None:
            return None
        chemins_init[a] = chemin

    racine = Noeud(contraintes_init, chemins_init)
    frontiere = [(racine.cout, next(compteur), racine)]

    while frontiere:
        _, _, noeud = heapq.heappop(frontiere)

        conflit = trouver_conflit(noeud.chemins)

        if conflit is None:
            return noeud.chemins  # solution trouvée, sans conflit

        a1, a2 = conflit["agents"]

        for agent_contraint in (a1, a2):
            nouvelles_contraintes = {
                a: (set(v[0]), set(v[1])) for a, v in noeud.contraintes.items()
            }
            sommets, aretes = nouvelles_contraintes[agent_contraint]

            if conflit["type"] == "sommet":
                sommets.add((conflit["pos"], conflit["temps"]))
            else:
                if agent_contraint == a1:
                    aretes.add((conflit["pos_avant"], conflit["pos_apres"], conflit["temps"]))
                else:
                    aretes.add((conflit["pos_apres"], conflit["pos_avant"], conflit["temps"]))

            depart, but = agents[agent_contraint]
            nouveau_chemin = a_star(grille, depart, but, sommets, aretes, horizon=20)

            if nouveau_chemin is None:
                continue  # branche impossible, on l'abandonne

            nouveaux_chemins = dict(noeud.chemins)
            nouveaux_chemins[agent_contraint] = nouveau_chemin

            enfant = Noeud(nouvelles_contraintes, nouveaux_chemins)
            heapq.heappush(frontiere, (enfant.cout, next(compteur), enfant))

    return None  # pas de solution


# ---------- Exemple d'utilisation ----------

if __name__ == "__main__":
    grille = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    agents = {
        "A": ((0, 0), (3, 0)),
        "B": ((3, 0), (0, 0)),
    }

    solution = cbs(grille, agents)

    if solution:
        for agent, chemin in solution.items():
            print(f"{agent}: {chemin}")
    else:
        print("Aucune solution trouvée.")
