#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, p_age: int) -> None:
        if (height < 0 or p_age < 0):
            print("Erreur init OBJ plante")
            self._name = name
            self._height = 0.0
            self._p_age = 0
        else:
            self._name = name
            self._height = round(height, 1)
            self._p_age = p_age

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._p_age = self._p_age + 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._p_age} days old")

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Height update rejected")
        else:
            self._height = round(height, 1)
            print(f"Height update: {self._height}cm")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Height update rejected")
        else:
            self._p_age = int(age)
            print(f"Age update: {self._p_age} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._p_age)


def ft_garden_security() -> None:
    plante = Plant("Rose", 15, 10)
    print("Plante created: ",  end="")
    plante.show()
    print("")
    plante.set_height(25)
    plante.set_age(30)
    print("")
    plante.set_age(-30)
    plante.set_height(-16)
    print("\nCurrent state: ", end="")
    plante.show()


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security()
