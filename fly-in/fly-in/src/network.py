from src.zones.normal_zone import NormalZone
from .zones.zone import Zone
from .connection import Connection


class Network:
    """ class Network qui assemble les zones pour cree un reseau"""
    def __init__(self) -> None:
        """ initialisation de la class Network"""
        self.all_zone: dict[str, Zone] = {}
        self.all_connection: list[Connection] = []
        self.nbr_drone: int = 0
        self.start_zone: Zone = NormalZone('start', (0, 0),
                                           self.nbr_drone)
        self.end_zone: Zone = NormalZone('end', (0, 0),
                                         self.nbr_drone)

    def add_zone(self, zone: Zone) -> None:
        """ Ajout et initialisation de zone """
        self.all_zone.update({zone.name: zone})

    def add_connection(self,
                       connection: tuple[str, str],
                       max_link: int = 1) -> None:
        """Ajoute initialiser et relier la connection provenant
          du fichier parser qui est encore du text"""

        zone_a, zone_b = connection
        try:
            connect_zone: Connection = Connection(
                                       self.all_zone[zone_a.strip()],
                                       self.all_zone[zone_b.strip()],
                                       max_link)
            self.all_connection.append(connect_zone)
        except Exception:
            raise KeyError('Got error: zone does not exist!')

    def set_start(self, start: Zone) -> None:
        """ Ajouter une valeur a start"""
        self.start_zone = start
        self.add_zone(self.start_zone)

    def set_end(self, end: Zone) -> None:
        """ Ajouter une valeur a end """
        self.end_zone = end
        self.add_zone(self.end_zone)

    def set_nbr_drone(self, nbr_drone: int) -> None:
        """ Ajouer une valeur au nbr de drone"""
        self.nbr_drone = nbr_drone

    def get_neighbor(self, zone_name: str) -> list[Connection]:
        """ Recuperer les voisins d'une zone precise"""
        list_neighbor: list[Connection] = []
        for zone in self.all_connection:
            if (zone_name in (zone.zone_a.name, zone.zone_b.name)):
                list_neighbor.append(zone)
        return list_neighbor
