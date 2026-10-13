from src.parser import Parser
import os
from dotenv import load_dotenv


if __name__ == '__main__':

    try:
        load_dotenv()
        path = os.environ.get("PATH_MAP")    
        with open(path, 'r') as f:
            pars = Parser(f)
            pars._parse_nb_drones_line()
            pars._parse_zone_line()
            pars._parse_connection_line()
            print(pars.graph.all_zone)
            print(pars.graph.all_connection)
    except Exception as e:
        print(e)
