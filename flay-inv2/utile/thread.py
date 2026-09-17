3. Algorithme étape par étape
Initialiser : distance[start] = 0, distance[toutes les autres] = infini
Créer une file de priorité (min-heap) contenant (0, start)
Tant que la file n'est pas vide :
Extraire la zone courant avec le plus petit coût connu
Si courant == end → terminé, chemin trouvé
Pour chaque voisin de courant avec coût d'arête w :
nouveau_coût = distance[courant] + w
Si nouveau_coût < distance[voisin] → mettre à jour distance[voisin] et empiler (nouveau_coût, voisin)
Reconstruire le chemin en gardant, pour chaque zone, un pointeur vers le "prédécesseur" qui a permis d'obtenir son meilleur coût
4. Pourquoi une file de priorité (min-heap) ?

Parce qu'on veut toujours traiter ensuite la zone la moins chère parmi celles en attente, sans devoir retrier toute la liste à chaque tour. En Python, ça correspond au module heapq.
