#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, p_age: int) -> None:
        if (height < 0 or p_age < 0):
            print("Erreur init OBJ")
            self._name = "Unknow Plante"
            self._height = 0.0
            self._p_age = 0
        else:
            self._name = name
            self._height = height
            self._p_age = p_age

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._p_age = self._p_age + 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._p_age} days old")

    def set_height(self, height: float) -> None:
        if (height < 0):
            print("Error, height value is wrong")
        else:
            self._height = height
            print(f"Height update: {self._height}")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print("Error, age value is wrong")
        else:
            self._p_age = age
            print(f"Age update: {self._p_age}")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._p_age)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int,
            color: str
            ) -> None:
        super().__init__(name, height, p_age)
        self._color = color
        self._isbloom = False

    def set_color(self, color: str) -> None:
        self._color = color

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self._isbloom = True

    def show(self) -> None:
        super().show()
        print(f"color: {self._color}")
        if (not self._isbloom):
            print(f"{self._name} has not bloomed yet!")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, p_age)
        self._trunk_diameter = round(trunk_diameter, 1)

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = round(trunk_diameter, 1)

    def get_trunk_diameter(self) -> float:
        return (round(self._trunk_diameter, 1))

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")

    def show(self) -> None:
        super().show()
        print(f"trunk diameter: {self._trunk_diameter}")


class Vegetable(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                p_age: int,
                harvest_season: str,
                nutritional_value: float
                ) -> None:
        super().__init__(name, height, p_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season

    def grow(self) -> None:
        super().grow()
        self._nutritional_value = self._nutritional_value + 1

    def set_nutritional_value(self, nutritional_value: float) -> None:
        self._nutritional_value = nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    def show(self) -> None:
        super().show()
        print(f"harvest season: {self._harvest_season}")
        print(f"nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    print("=== Vegetable")
    tomate = Vegetable("Tomato", 5, 10, "Avril", 0)
    for i in range(20):
        tomate.grow()
        tomate.age()
    tomate.show()

    print("\n=== Flower")
    Rose = Flower("Rose", 15, 10, "red")
    Rose.show()
    Rose.bloom()
    Rose.show()

    print("\n=== Tree")

    Oak = Tree("Oak", 200, 365, 5.0)
    Oak.show()
    Oak.produce_shade()
    print(f"{Oak._name} Oak now produces a shade ", end="")
    print(f"of {Oak.get_height()} long and {Oak.get_trunk_diameter()}cm wide.")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()