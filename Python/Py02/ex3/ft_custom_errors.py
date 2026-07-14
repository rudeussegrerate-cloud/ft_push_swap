#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise PlantError("la temperatur est trop froid")
    if (temp > 40):
        raise PlantError("la temperatur est trop chaud")
    return (temp)


def water_test(water_qty: int) -> None:
    if water_qty < 2:
        raise WaterError("Erreur, manque d'eau")


def test(erreur: int) -> None:
    if erreur == 0:
        input_temperature("-50")
    elif erreur == 1:
        water_test(1)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    i = 0
    a = '\n'
    error_list = [PlantError, WaterError, GardenError, GardenError]
    while i < 4:
        try:
            if (i < 2):
                print(f"Testing {error_list[i].__name__}...")
            elif (i == 2):
                print("Testing catching all garden errors...")
            test(i % 2)
        except error_list[i] as e:
            if i == 2:
                a = ''
            print(f"Caught {error_list[i].__name__}: {e}{a}")
        i += 1

    print("\nAll custom error types work correctly!")
