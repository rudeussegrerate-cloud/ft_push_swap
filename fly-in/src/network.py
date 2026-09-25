from .zones.zone import Zone
from .connection import Connection


class Network:
    """ class Network qui assemble les zones pour cree un reseau"""
    def __init__(self) -> None:
        """ initialisation de la class Network"""
        self.all_zone: dict[str, Zone] = {}
        self.all_connection: list[Connection] = []

    def add_zone(self, zone: Zone) -> None:
        """Ajout et initialisation de zone """
        self.all_zone.update({zone.name: zone})

    def add_connection(self,
                       connection: tuple[str, str],
                       max_link: int = 1) -> None:
        """Ajoute initialiser et relier la connection provenant
          du fichier parser qui est encore du text"""

        zone_a, zone_b = connection
        try:
            connect_zone: Connection = Connection(self.all_zone[zone_a],
                                                  self.all_zone[zone_b],
                                                  max_link)
            self.all_connection.append(connect_zone)
        except Exception:
            raise KeyError('Got error: zone does not exist!')

    def get_neighbor(self, zone_name: str) -> list[Connection]:
        """ Recuperer les voisins d'une zone precise"""
        list_neighbor: list[Connection] = []
        for zone in self.all_connection:
            if (zone_name in (zone.zone_a.name, zone.zone_b.name)):
                list_neighbor.append(zone)
        return list_neighbor
