from .model import Zone

class NormalZone(Zone):
    def __init__(self, capacity: int = 1):
        super().__init__(1, capacity)


class PriorityZone(Zone):
    def __init__(self, capacity: int = 1):
        super().__init__(1, capacity)
        self._priority = True


class RestrictedZone(Zone):
    def __init__(self, capacity: int = 1):
        super().__init__(2, capacity)


class BlockedZone(Zone):
    def __init__(self, capacity: int = 1):
        super().__init__(0, capacity)




class Connection():
    def __init__(self):
        self._zone: dict = {}
        self._capacity = 0

    def set_capacity(self, nbr):
        self._capacity = nbr


class Drone():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._list_move:list[int] = [0, 1, 2]
        self._position:list[int, int] = [0, 0]

    



class Network():
    def __init__(self, zone: Zone, connexion: Connection):
        self._zone: list[Zone] = zone
        self._connexion: list[Connection] = connexion


class Parser():
    pass


class Pathfinding():
    pass


class ReservationTable():
    pass


class ConflictChecker():
    pass


class Simulation():
    pass


class Display():
    pass

