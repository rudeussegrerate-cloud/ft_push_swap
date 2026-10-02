from src.parser import Parser


if __name__ == '__main__':
    with open('/home/tusandri/Cursus42/Python/fly-in/fly-in/maps/easy/01_linear_path.txt', 'r') as f:
        pars = Parser(f)
        pars._parse_nb_drones_line()
        pars._parse_zone_line()
        print(pars.graph.nbr_drone)

