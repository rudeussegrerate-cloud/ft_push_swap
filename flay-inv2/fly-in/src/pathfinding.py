import heapq
import math

# 1. Définition de l'heuristique : distance à vol d'oiseau entre deux nœuds
def heuristique(position_a, position_b):
    xa, ya = position_a
    xb, yb = position_b
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)


def algorithme_a_star(graphe, positions, depart, arrivee):
    # File de priorité (stocke des tuples : (f_score, noeud))
    a_explorer = []
    heapq.heappush(a_explorer, (0, depart))
    
    # Dictionnaires pour stocker les coûts et la provenance
    provenance = {}
    g_score = {noeud: float('inf') for noeud in graphe}
    g_score[depart] = 0
    
    f_score = {noeud: float('inf') for noeud in graphe}
    f_score[depart] = heuristique(positions[depart], positions[arrivee])

    while a_explorer:
        # On extrait le nœud avec le plus petit f_score
        _, actuel = heapq.heappop(a_explorer)

        # Si on a atteint la cible, on reconstruit le chemin
        if actuel == arrivee:
            chemin = []
            while actuel in provenance:
                chemin.append(actuel)
                actuel = provenance[actuel]
            chemin.append(depart)
            return chemin[::-1] # Inverser pour avoir le chemin du départ à l'arrivée

        # Exploration des voisins
        for voisin, poids in graphe[actuel].items():
            # Coût pour aller chez le voisin en passant par le nœud actuel
            g_temporaire = g_score[actuel] + poids
            
            if g_temporaire < g_score[voisin]:
                # Ce chemin est meilleur que le précédent trouvé, on l'enregistre !
                provenance[voisin] = actuel
                g_score[voisin] = g_temporaire
                f_score[voisin] = g_temporaire + heuristique(positions[voisin], positions[arrivee])
                
                # S'il n'est pas déjà dans la file, on l'ajoute
                if voisin not in [n[1] for n in a_explorer]:
                    heapq.heappush(a_explorer, (f_score[voisin], voisin))

    return None

graphe_routier = {
    'Paris': {'Lyon': 460, 'Lille': 220},
    'Lille': {'Paris': 220, 'Strasbourg': 520},
    'Lyon': {'Paris': 460, 'Strasbourg': 490, 'Marseille': 310},
    'Strasbourg': {'Lille': 520, 'Lyon': 490, 'Marseille': 800},
    'Marseille': {'Lyon': 310, 'Strasbourg': 800}
}

# Coordonnées fictives (x, y) pour calculer la distance à vol d'oiseau (heuristique)
positions_villes = {
    'Paris': (2, 5),
    'Lille': (2.5, 7),
    'Lyon': (4, 2),
    'Strasbourg': (6, 5.5),
    'Marseille': (4.5, 0)
}

# --- Test ---
chemin_optimal = algorithme_a_star(graphe_routier, positions_villes, 'Paris', 'Marseille')
print("Chemin le plus court trouvé par A* :", chemin_optimal)

