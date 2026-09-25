from typing import IO
from .zones.blocked_zone import BlockedZone
from .zones.normal_zone import NormalZone
from .zones.priority_zone import PriorityZone
from .zones.restricted_zone import RestrictedZone
from .network import Network
import re


class Parser:
    def __init__(self, file:IO[str]):
        self.graph = Network()
        self.open_file = file
        
    def _parse_zone_line(self):
        zone_type: dict = {'restricted': RestrictedZone, 'priority':PriorityZone, 'Normal': NormalZone, 'Blocked': BlockedZone}
        data = self.open_file.readlines()
        for d in data:
            if ('start_hub', 'hub', 'End_hub') in d:
                zone, _ = d.split(':')
                self.graph.add_zone(zone_type[zone.lower()])

    def _parse_connection_line(self):
        data = self.open_file.readlines()
        z1, z2 = '', ''
        max_link = re.findall(r'\[([^\]]*)\]', self.open_file.read())

        for d in data:
            if 'connection' in data:
                con = d.split(':')
                for c in con[1]:
                    z1, z2 = c.split('-')

        self.graph.all_connection((z1, z2), max_link)

    def _parse_nb_drones_line(self) -> int | None:
        data = self.open_file.readlines()
        for d in data:
            if ('nbr_drone' in d):
                _, nbr = d.split(':')
                return nbr
        return None
