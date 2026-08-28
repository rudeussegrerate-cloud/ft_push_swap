from typing import Any
from algorithm import is_path

def extact_zone(all: str) -> str:
    return all.split()[0]


def extract_coord(all: str) -> tuple[int, int]:
    data: list[int]= []
    count = 0
    for coord in all.split():
        try:
            data.append(int(coord))
            count+= 1
        except Exception:
            pass
    if count > 2 or count < 2:
        raise Exception("Got error: coordinate must be two for x and y")
    return tuple(data)


def extract_metadata(all: str) -> list[dict] | None:
    value = ""
    debut = all.find('[')
    fin = all.find(']')
    value = all[debut+1 : fin]

    if (debut == -1 and fin !=-1) or (fin == -1 and debut != -1):
        raise Exception("Got error: A hook is missing;p!")
    if debut == -1 and fin == -1:
        return [{'zone': 'normal'}, {'color': None}, {'max_drones': 1}]
    arg = []
    for elem in value.strip().split():
        val = elem.split('=')
        arg.append({val[0] : val[1]})

    return arg


from collections import deque

def algo_path(graph, start):
    visited = deque()
    visited.append(start)
    left_visit = []
    while visited:
        node = visited.pop()
        left_visit.append(node)
        for adj in graph[node]:
            if adj not in left_visit:
                visited.append(adj)
    print(left_visit)

from collections import defaultdict
 
if __name__ == "__main__":
    d = []
    with open("maps/easy/01_linear_path.txt", "r") as f:
        textes = f.readlines()
        for text in textes:
            try:
                arg = text.rstrip().split(":")
                if '#' not in text:
                    d.append((arg[0].strip(), arg[1].strip()))
            except (IndexError , Exception):
                pass
        # print(d, "\n")

    nbr_drones = 0
    start = []
    hub = []
    end = []
    connexion =  defaultdict(list)

    #zone index0, coordonner index1, metadata index2
    for key, elem in d:
        if (key == 'start_hub'):
            start.append((extact_zone(elem), extract_coord(elem), extract_metadata(elem)))
        if (key == 'hub'):
            hub.append((extact_zone(elem), extract_coord(elem), extract_metadata(elem)))
        if (key == 'end_hub'):
            end.append((extact_zone(elem), extract_coord(elem), extract_metadata(elem)))
        if (key == 'connection'):
            arg = str(elem).split('-')
            noeud_a = arg[0].strip()
            noeud_b = arg[1].strip()
            connexion[noeud_a].append(noeud_b)

algo_path(connexion, 'start')

