class GardenError(Exception):
	def __init__(self, message = "Erreur, Plante inconnue :("):
		super().__init__(message)


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def water_plant(plant_name: str) -> str:
    if (plant_name != plant_name.capitalize()):
        print("[OK]")
        plant_name = plant_name.capitalize()
        return (plant_name)
    else:
        raise WaterError("Erreur, plante non arroser :(")
    return (plant_name)
def test_watering_system():
    print("== Opens the watering system ==")
    test_list = ("tomate", "lettuce", "carrots", "tomato", "1ettuce")
    for test in test_list:
        try:
            water_plant(test)
        except WaterError as e:
            print(f"{e}")

test_watering_system()