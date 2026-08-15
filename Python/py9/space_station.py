from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError
except (ImportError, ModuleNotFoundError):
    print("Install module pydantic")
    exit(1)

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name:str = Field(min_length=1, max_length=50)
    crew_size:int = Field(ge=1, le=20)
    power_level:float = Field(ge=0.0, le=100.0)
    oxygen_level:float = Field(ge=0.0, le=100.0)
    last_maintenance:datetime = Field(...)
    is_operational:bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)



def main() -> None:
    data=   {
            "station_id": "QCH189",
            "name": "Deep Space Observatory",
            "crew_size": 30,
            "power_level": 70.8,
            "oxygen_level": 88.1,
            "last_maintenance": "2023-08-24T00:00:00",
            "is_operational": False,
            "notes": "System diagnostics required"
        }
    try:
        station = SpaceStation.model_validate(data)

        print(f"{station.station_id}")
        print(f"{station.crew_size}")
    except ValidationError as e:
        print(f"{e.errors()[0].get('msg')}") # Maka ila message d'erreur ao antin'ilay ValidationError
                                             # ilay e.errors(): liste dict
                                             # de mila sikirina ao mintsy le type an erreur
                                             # io ny fomba fakana azy
                                             # e.errors()[0]: maka ilay position 0
                                             # sarty is dict, dia afaka alaina ilay valeur aoa anatiny
                                             # 'msg' io ny cleany de le get no maka azy
main()