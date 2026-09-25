from .zones.zone import Zone


class Connection:
    """ class pour relier les zone """
    def __init__(self,
                 zone_a: Zone,
                 zone_b: Zone,
                 max_link_capacity: int = 1) -> None:
        """ initialisation de la valeur des attibue de connexion """
        self.max_link_capacity: int = max_link_capacity
        self.zone_a: Zone = zone_a
        self.zone_b: Zone = zone_b

    def get_link(self) -> str:
        """afficher la connexion etablie entre les zone concerner"""
        return f"{self.zone_a.name}-{self.zone_b.name}"
