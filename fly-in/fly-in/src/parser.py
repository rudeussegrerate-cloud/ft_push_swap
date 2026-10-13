from typing import IO, Any
from .zones.blocked_zone import BlockedZone
from .zones.normal_zone import NormalZone
from .zones.priority_zone import PriorityZone
from .zones.restricted_zone import RestrictedZone
from .network import Network


class Parser:
    """Parse un fichier de configuration pour construire un Network.

    Les méthodes _parse_nb_drones_line, _parse_zone_line et
    _parse_connection_line doivent être appelées dans cet ordre
    précis par l'appelant (main.py), car les connexions référencent
    des zones qui doivent déjà exister dans le Network.
    """
    def __init__(self, file: IO[str]):
        """ initialisation des attribue de Parser"""
        self.graph: Network = Network()
        self.open_file: IO[str] = file
        self.zone_type: dict[str, Any] = {'priority': PriorityZone,
                                          'restricted': RestrictedZone,
                                          'normal': NormalZone,
                                          'blocked': BlockedZone}

    def _parse_zone_line(self) -> None:
        """Extrait les zone pour chaque ligne du fichier"""
        text: str = self.open_file.readline()
        zone_param: list[str] = []
        while (text):
            if ('#' not in text and 'connection' not in text):
                zone_param = text.strip().split(':')
                if text not in ('\n', '#'):
                    try:
                        parma_tbv = zone_param[1].split()
                        meta_data = self._parse_metadata(text)
                        zone = self.zone_type[meta_data['zone']]
                        self.graph.add_zone(zone(parma_tbv[0],
                                            (int(parma_tbv[1]),
                                            int(parma_tbv[2])),
                                            meta_data['max_drone'],
                                            meta_data['color']))
                    except IndexError:
                        pass
                    except KeyError:
                        zone = self.zone_type['normal']
                        self.graph.add_zone(zone(parma_tbv[0],
                                            (int(parma_tbv[1]),
                                            int(parma_tbv[2])),
                                            meta_data['max_drone'],
                                            meta_data['color']))
            text = self.open_file.readline()
        self.open_file.seek(0)

    def _parse_connection_line(self) -> None:
        """Extrait une connection pour chaque ligne du fichier"""
        text = self.open_file.readline()
        while (text):
            if ('#' not in text and 'connection' in text):
                zone_param = text.split(':')
                meta_data = self._parse_metadata(text)
                c1, c2 = zone_param[1].split('-')
                if '[' in c2:
                    c2 = c2.split()[0]
                self.graph.add_connection((c1, c2),
                                          int(meta_data['max_link_capacity']))
            text = self.open_file.readline()
        self.open_file.seek(0)

    @staticmethod
    def _parse_metadata(raw: str) -> dict[str, str]:
        """Fonction utile pour l'extraction des metadata"""
        data_list: dict[str, Any] = {'zone': 'normal',
                                     'color': None,
                                     'max_drone': 1,
                                     'max_link_capacity': 1}
        if '#' not in raw:
            try:
                debut = raw.index("[") + 1
                fin = raw.index("]")
                data: list[str] = raw[debut:fin].strip().split(' ')
            except (ValueError, Exception, Exception):
                return data_list
            else:
                for d in data:
                    dk, dv = d.split('=')
                    data_list.update({dk: dv})
        return data_list

    def _parse_nb_drones_line(self) -> None:
        """ fonction pour extrait le nombre de drone"""
        text = self.open_file.readline().split(':')
        while (text):
            if (text[0] == 'nb_drones'):
                self.graph.set_nbr_drone(int(text[1].strip()))
                break
            text = self.open_file.readline().split(':')
        self.open_file.seek(0)
