import heapq
import sys
from collections import deque


def is_path(graphe: dict, sommet_depart:str) -> tuple[bool, list[str]]:

    """
    Réalise un parcours en largeur (BFS) d'un graphe à partir d'un sommet donné.
    Retourne la liste des sommets dans l'ordre de leur visite.
    """
    # Liste pour mémoriser l'ordre des sommets visités
    visites = []
    
    # Utilisation d'un ensemble (set) pour des vérifications d'existence ultra-rapides
    deja_vus = set()
    
    # Initialisation de la file FIFO avec le sommet de départ
    file = deque([sommet_depart])
    deja_vus.add(sommet_depart)
    
    while file:
        # On défile le premier sommet de la file
        sommet_courant = file.popleft()
        visites.append(sommet_courant)
        
        # On explore tous les voisins du sommet courant
        for voisin in graphe[sommet_courant]:
            if voisin not in deja_vus:
                deja_vus.add(voisin)
                file.append(voisin)  # On enfile le voisin non visité
                
    return visites



def dijkstra(adj, src):

    V = len(adj)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    dist = [sys.maxsize] * V

    # Distance from source to itself is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # Process the queue until all reachable vertices are finalized
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > dist[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adj[u]:

            # If we found a shorter path to v through u, update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    # Return the final shortest distances from the source
    return dist


if __name__ == "__main__":
    src = 0
    
    adj = [
        [(1, 4), (2, 8)],
        [(0, 4), (4, 6), (2, 3)],
        [(0, 8), (3, 2), (1, 3)],
        [(2, 2), (4, 10)],
        [(1, 6), (3, 10)]
    ]
    
    result = dijkstra(adj, src)
    print(*result)

