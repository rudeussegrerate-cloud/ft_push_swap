from typing import IO, Any

from src.zones.zone import Zone
from .zones.blocked_zone import BlockedZone
from .zones.normal_zone import NormalZone
from .zones.priority_zone import PriorityZone
from .zones.restricted_zone import RestrictedZone
from .network import Network
import re


class Parser:
    def __init__(self, file: IO[str]):
        self.graph: Network = Network()
        self.open_file: IO[str] = file
        self.zone_type: dict = {'priority': PriorityZone,
                                'restricted': RestrictedZone,
                                'normal': NormalZone,
                                'blocked': BlockedZone}

    def _parse_zone_line(self) -> None:
        text: str = self.open_file.readline()
        zone_param: tuple[str]= ()
        self.graph.set_start()
        self.graph.set_end()
        while (text):
            if ('#' not in text and 'connection' not in text):
                zone_param = text.split(':')
                parma_tbv = zone_param[1].split(' ', 4)
                meta_data = self._parse_metadata(text)
                zone = self.zone_type[meta_data['type']]
                self.graph.add_zone(zone(parma_tbv[0], (parma_tbv[1], parma_tbv[2]), meta_data['max_link'], meta_data['color']))
            text = self.open_file.readline()

    def _parse_connection_line(self) -> None:
        text = self.open_file.readline()
        while(text):
            if ('#' not in text):
                zone_param = text.split(':')
                meta_data = self._parse_metadata(text)
                self.graph.add_connection(zone_param[1].split('-'), int(meta_data['max_link']))
            text = self.open_file.readline()

    @staticmethod
    def _parse_metadata(raw: str) -> dict[str, str]:
        data_list: dict[str, str] = {}
        if '#' not in raw:
            debut = raw.index("[") + 1
            fin = raw.index("]")
            data: tuple[str, str] = raw[debut:fin].strip().split(' ')
            for d in data:
                dk, dv = d.split('=')
                data_list.update({dk: dv})
        return data_list


    def _parse_nb_drones_line(self) -> None:
        text = self.open_file.readline().split(':')
        while(text):
            if (text[0] == 'nbr_drones'):
                self.graph.set_nbr_drone(int(text[1].strip()))
