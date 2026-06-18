class GardenError(Exception):
	def __init__(self, message: str = "Erreur, Plante inconnue :(") -> None:
		super().__init__(message)


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def water_plant(plant_name: str) -> str:
    if (plant_name != plant_name.capitalize()):
        plant_name = plant_name.capitalize()
        print(f"Watering {plant_name}: [OK]")
        return (plant_name)
    else:
        raise WaterError(f"Erreur, plante :'{plant_name}' non arrosable :(")
    return (plant_name)


def test_watering_system() -> None:
    print("== Garden Watering System ==\n")
    test = ("tomate", "lettuce", "carrots", "tomato", "1ettuce")
    i = 0
    while (i < 5):
        try:
            if i == 0:
                print("Testing valide plane...")
                print("Opening watering system")
            elif (i == 3):
                print("Testing invalide plant...")
                print("Opening watering system")
            water_plant(test[i])
        except WaterError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
        finally:
            if i == 2 or i > 3:
                print("Closing watering system\n")
        i += 1
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()