from .zones.blocked_zone import BlockedZone
from .zones.normal_zone import NormalZone
from .zones.priority_zone import PriorityZone
from .zones.restricted_zone import RestrictedZone

class Parser:

    def _parse_zone_line(zone_list:list[str]):
        zone_type: dict = {'restricted': RestrictedZone, 'priority':PriorityZone, 'Normal': NormalZone, 'Blocked': BlockedZone}
        for zone in zone_list:
            
    def _parse_connection_line():
        pass

    def _parse_nb_drones_line():
        pass
