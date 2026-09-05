from algorithm import is_path
from pydantic import BaseModel, Field, ValidationError
import re
from element import Agent

class Zone(BaseModel):
    name: str
    pos: tuple[int, int]
    metadata: list[dict]


class Config(BaseModel):
    nb: int
    start: Zone
    hub: list[Zone]
    end: Zone
    con: str

nb_drone = 0

configuration = []
with open("maps/hard/01_maze_nightmare.txt", "r") as fconf:
    confs = fconf.readlines()
    for elem in confs:
        if "nb_drones" in elem:
            _, e = elem.split(':')
            nb_drone = int(e)
        if (elem.strip().rstrip() and "#" not in elem.strip().rstrip()):
            key, value = elem.rstrip().split(":")
            configuration.append((key.strip(), value.strip()))

start = {}
hub = []
end_hub = {}
con = {}


for key, value in configuration:
    if (key == "start_hub"):
        start = {key: value}
    elif (key == "hub"):
        hub.append((key, value))
    elif (key == "end_hub"):
        end_hub = {key:value}
    elif (key == "connection"):
        i,j = value.split("-")
        con.update({i:j})


a1 = Agent(0, "bubul", 'start' , con)
a2 = Agent(1, "bubul2", 'start', con)

print("chemin a1:", *a1.mystape())
print("chemin a2:", *a2.mystape())
print(*con )


Route = []#action de tout les agents a effectuer



mon_graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Lancement du parcours depuis le sommet 'A'
ordre_visite = is_path(mon_graphe, 'A')
print("Ordre de visite du parcours en largeur :", ordre_visite)
# Résultat attendu : ['A', 'B', 'C', 'D', 'E', 'F']
