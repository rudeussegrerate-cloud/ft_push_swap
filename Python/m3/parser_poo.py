import re
import sys
from typing import NamedTuple


class Zone(NamedTuple):
    """
    Représente une zone avec son nom, ses coordonnées et ses métadonnées.
    """
    name: str
    coordinates: tuple[int, int]
    zone_type: str = "normal"
    color: str = "none"
    max_drones: int = 1


class Connection(NamedTuple):
    """
    Représente une connexion bidirectionnelle entre deux zones.
    """
    zone_a: str
    zone_b: str
    max_link_capacity: int = 1


class InvalidConfigError(Exception):
    """Exception levée en cas d'erreur dans la configuration du fichier."""


class ConfigParser:
    """
    Responsable du chargement et de la conversion du fichier de configuration.
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.raw_data: list[tuple[str, str]] = []
        self._load_file()

    def _load_file(self) -> None:
        """
        Lit le fichier et extrait les paires clé-valeur.
        """
        with open(self.filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        self.raw_data.append(
                            (parts[0].strip(), parts[1].strip())
                            )

    @staticmethod
    def _parse_coordinates(raw_val: str) -> tuple[int, int]:
        """
        Extrait et valide les deux coordonnées numériques d'une zone.
        """
        # Ne conserver que la partie avant les métadonnées [...]
        clean_val = raw_val.split("[")[0].strip()
        tokens = clean_val.split()
        coord_tokens = tokens[1:]

        numbers: list[int] = []
        for token in coord_tokens:
            try:
                numbers.append(int(token))
            except ValueError:
                print(
                    "Zone coordinates must be integers "
                    f"found '{token}'"
                )
                sys.exit(1)

        if len(numbers) != 2:
            print(
                "Zone coordinates must contain two integers, "
                f"found {len(numbers)}"
            )
            sys.exit(1)

        return (numbers[0], numbers[1])

    @staticmethod
    def _parse_zone_metadata(raw_val: str) -> dict[str, str | int]:
        """
        Extrait les métadonnées de zone entre [...]
        et applique les valeurs par défaut.
        """
        metadata: dict[str, str | int] = {
            "zone": "normal",
            "color": "none",
            "max_drones": 1
        }

        match = re.search(r"\[(.*?)\]", raw_val)
        if not match:
            return metadata

        content = match.group(1)
        tags = re.findall(r"(\w+)=([^\s,]*)", content)
        for key, value in tags:
            if key == "zone":
                metadata["zone"] = value
            elif key == "color":
                metadata["color"] = value
            elif key == "max_drones" and value.isdigit() and int(value) >= 1:
                metadata["max_drones"] = int(value)
            else:
                raise InvalidConfigError("Max drones must be positive values")

        return metadata

    @staticmethod
    def _parse_connection(raw_val: str) -> Connection:
        """
        Parse une ligne de connexion
        type 'zoneA-zoneB [max_link_capacity=2]'.
        """
        # Séparation de la partie connexion et des métadonnées [...]
        match = re.search(r"\[(.*?)\]", raw_val)
        meta_content = match.group(1) if match else ""

        # Extraction de la capacité max
        max_capacity = 1
        cap_match = re.search(r"max_link_capacity=(\d+)", meta_content)
        if cap_match:
            max_capacity = int(cap_match.group(1))

        # Récupération de la partie sans les crochet
        # pour extraire zone_a et zone_b
        connection_part = raw_val.split("[")[0].strip()
        zones = [z.strip() for z in connection_part.split("-")]

        zone_a = zones[0] if len(zones) >= 1 else ""
        zone_b = zones[1] if len(zones) >= 2 else ""

        if len(zones) != 2:
            raise InvalidConfigError(
                "Connections must link only previously defined zones "
                "using connection: <zone1>-<zone2> [metadata]."
            )

        return Connection(
            zone_a=zone_a,
            zone_b=zone_b,
            max_link_capacity=max_capacity
            )

    def get_zones(self, key_filter: str) -> list[Zone]:
        """
        Retourne la liste des objets Zone correspondant à une clé donnée.
        """
        zones = []
        for key, val in self.raw_data:
            if key == key_filter:
                tokens = val.split()
                name = tokens[0] if tokens else ""
                coords = self._parse_coordinates(val)
                meta = self._parse_zone_metadata(val)

                zones.append(Zone(
                    name=name,
                    coordinates=coords,
                    zone_type=str(meta["zone"]),
                    color=str(meta["color"]),
                    max_drones=int(meta["max_drones"])
                ))

        return zones

    def get_connections(self) -> list[Connection]:
        """
        Retourne la liste des objets Connection.
        """
        connections = []
        for key, val in self.raw_data:
            if key == "connection":
                connections.append(self._parse_connection(val))
        return connections

    def get_nbr_drones(self) -> int:
        """
        Extrait et retourne le nombre total de drones sous forme d'entier.
        """
        for key, val in self.raw_data:
            if key == "nb_drones":
                # Extrait le premier nombre trouvé dans la valeur
                numbers = [
                    int(token) for token in val.split() if token.isdigit()
                    ]
                if numbers:
                    return numbers[0]
        return 0

    def validate(self) -> None:
        """Vérifie l'intégrité de la configuration.
        Vérifications :
        - Les coordonnées sont toutes des entiers
        (garanti par le typage de _parse_coordinates).
        - Il existe exactement une zone de départ ('start_hub').
        - Il existe exactement une zone d'arrivée ('end_hub').
        """
        start_zones = self.get_zones("start_hub")
        end_zones = self.get_zones("end_hub")
        hub_zones = self.get_zones("hub")
        connection_list = self.get_connections()
        nbr_drones = self.get_nbr_drones()

        name: list[str] = []
        name.append(start_zones[0].name)
        name.append(end_zones[0].name)
        for elem in hub_zones:
            name.append(elem.name)

        nbr_start = start_zones[0].max_drones
        nbr_end = end_zones[0].max_drones
        
        if nbr_drones > nbr_start or nbr_end < nbr_drones:
            raise InvalidConfigError (
                "Max drones must be greater or equal than number drones!"
            )

        if len(start_zones) != 1:
            raise InvalidConfigError(
                f"The configuration must contain exactly one start zone."
                f"'start_hub' (found : {len(start_zones)})."
            )

        if len(end_zones) != 1:
            raise InvalidConfigError(
                f"The configuration must contain exactly one destination zone."
                f"'end_hub' (found : {len(end_zones)})."
            )
        for conn in connection_list:
            zone_1 = conn.zone_b
            zone_2 = conn.zone_a
            if zone_1 not in name or zone_2 not in name:
                raise InvalidConfigError(
                    "Invalid hub name!!!"
                )
            comp = (zone_1, zone_2, conn.max_link_capacity)
            if comp in connection_list:
                raise InvalidConfigError(
                  "Connections must link only previously defined zones "
                  "using connection: <zone1>-<zone2> [metadata]."
                )
        if nbr_drones == 0:
            raise InvalidConfigError(
                "Capacity values must be positive integers."
            )


if __name__ == "__main__":
    path = ["maps/medium/02_circular_loop.txt",
            "maps/medium/01_dead_end_trap.txt",
            "maps/medium/03_priority_puzzle.txt",
            "maps/easy/01_linear_path.txt",
            "maps/easy/02_simple_fork.txt",
            "maps/easy/03_basic_capacity.txt",
            "maps/hard/01_maze_nightmare.txt",
            "maps/hard/02_capacity_hell.txt",
            "maps/hard/03_ultimate_challenge.txt",
            "maps/challenger/01_the_impossible_dream.txt"
            ]
    file_path = path[0]

    try:
        parser = ConfigParser(file_path)

        start_zones: list[Zone] = parser.get_zones("start_hub")
        hub_zones: list[Zone] = parser.get_zones("hub")
        end_zones: list[Zone] = parser.get_zones("end_hub")
        connection_list: list[Connection] = parser.get_connections()
        nbr_drones = parser.get_nbr_drones()

        print("=== CHECK CONFIG ===")
        parser.validate()
        print("Configuration valide !")

        print("\n=== NUMBER OF DRONES ===")
        print(f"Number of drones : {nbr_drones}")

        print("=== STARTS ===")
        for zone in start_zones:
            print(
                f"Name: {zone.name} | Coords: {zone.coordinates} "
                f"| Type: {zone.zone_type} | Color: {zone.color} "
                f"| Max Drones: {zone.max_drones}"
            )

        print("\n=== HUBS ===")
        for zone in hub_zones:
            if zone.max_drones >= 1:
                print(
                    f"Name: {zone.name} | Coords: {zone.coordinates} "
                    f"| Type: {zone.zone_type} | Color: {zone.color} "
                    f"| Max Drones: {zone.max_drones}"
            )
            else:
                raise InvalidConfigError(f"Max drones must be >= 1, found: {zone.max_drones}")

        print("\n=== ENDS ===")
        for zone in end_zones:
            print(
                f"Name: {zone.name} | Coords: {zone.coordinates} "
                f"| Type: {zone.zone_type} | Color: {zone.color} "
                f"| Max Drones: {zone.max_drones}"
            )

        print("\n=== CONNECTIONS ===")
        for conn in connection_list:
            zone_1 = conn.zone_b
            zone_2 = conn.zone_a
            comp: tuple[str, str, int] = (zone_1,
                                          zone_2,
                                          conn.max_link_capacity)
            print(
                f"Link: {conn.zone_a} <-> {conn.zone_b} "
                f"| Max Link Capacity: {conn.max_link_capacity}"
            )

    except (FileNotFoundError, InvalidConfigError) as e:
        print(f"Erreur : {e}")
