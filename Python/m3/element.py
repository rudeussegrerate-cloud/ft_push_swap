from algorithm import is_path


class Agent():
    def __init__(self, id = None, nom = None, start:str = None, graph: dict = None):
        self._id = id
        self._nom = nom
        _, self._rout = (is_path(graph, start))
        self._stape =(0, 1, 2)

    def mystape(self):
        return self._rout
    
