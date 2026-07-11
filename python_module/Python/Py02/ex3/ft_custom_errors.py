class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test(temp: int) -> None:
    if (temp == 0):
        raise PlantError("la temperatur est trop froid")
    elif (temp == 1):
        raise WaterError("Erreur, manque d'eau")


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
