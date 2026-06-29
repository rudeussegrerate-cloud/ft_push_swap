#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, p_age: int) -> None:
        self._name = name
        self._height = round(height, 1)
        self._p_age = p_age
        self.up_grow = 0.4
        self._stat = Plant.stat()

    class stat:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def set_grow(self, grow: int) -> None:
            self._grow = self._grow + grow

        def set_age(self, age: int) -> None:
            self._age = self._age + age

        def set_show(self, show: int) -> None:
            self._show = self._show + show

        def get_grow(self) -> int:
            return (self._grow)

        def get_age(self) -> int:
            return (self._age)

        def get_show(self) -> int:
            return (self._show)

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown Plant", 0.0, 0)

    @staticmethod
    def is_a_year(age: int) -> bool:
        return (age > 364)

    def grow(self) -> None:
        if self._name == "Rose":
            self.up_grow = 0.8
        elif self._name == "Sunflower":
            self.up_grow = 0.5
        elif self._name == "Cactus":
            self.up_grow = 0.2
        self._height = round(self._height + self.up_grow, 1)
        self._stat.set_grow(1)

    def age(self) -> None:
        self._p_age = self._p_age + 1
        self._stat.set_age(1)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._p_age} days old")
        self._stat.set_show(1)

    def set_height(self, height: float) -> None:
        if (height < 0):
            print("Error, height value is wrong")
        else:
            self._height = height
            print(f"Height update: {self._height}")

    def set_age(self, age: int) -> None:
        if (self.is_a_year(age)):
            print("Error, age value is wrong")
        else:
            self._p_age = age
            print(f"Age update: {self._p_age}")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._p_age)

    def stat_plant(self) -> None:
        print(f"[statistics for {self._name}]")
        print(f"Stats: {self._stat.get_show()} show", end="")
        print(f", {self._stat.get_grow()} grow, {self._stat.get_age()} age")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 p_age: int,
                 color: str
                 ) -> None:
        super().__init__(name, height, p_age)
        self._color = color
        self._IsBloom = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, value: str) -> None:
        self._color = value

    def bloom(self) -> None:
        self._IsBloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._IsBloom:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 p_age: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, p_age)
        self._trunk_diameter = trunk_diameter
        self._stati = Tree.stat()

    class stat(Plant.stat):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def get_shade(self) -> int:
            return self._shade

        def set_shade(self) -> None:
            self._shade = self._shade + 1

    def produce_shader(self) -> None:
        print(f"Tree {self._name} now produces a shade ", end="")
        print(f"of {self._height} long and {self._trunk_diameter} wide.")
        self._stati.set_shade()

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, value: int) -> None:
        self._trunk_diameter = value

    def show(self) -> None:
        super().show()
        print(f"trunk diameter: {self._trunk_diameter}")

    def stat_plant(self) -> None:
        super().stat_plant()
        print(f"{self._stati.get_shade()} shade")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 p_age: int,
                 harvest_season: str,
                 nutritional_value: float
                 ) -> None:
        super().__init__(name, height, p_age)
        self._harvest_season = harvest_season
        self._nutritional_value = round(nutritional_value, 1)

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def grow(self) -> None:
        super().grow()
        self._nutritional_value = self._nutritional_value + 1

    def set_harvest_season(self, value: str) -> None:
        self._harvest_season = value

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    def set_nutritional_value(self, value: float) -> None:
        self._nutritional_value = value

    def show(self) -> None:
        super().show()
        print(f"harvest season: {self._harvest_season}")
        print(f"nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 p_age: int,
                 color: str
                 ) -> None:
        super().__init__(name, height, p_age, color)
        self._graine = 0

    def get_graine(self) -> int:
        return self._graine

    def set_graine(self, value: int) -> None:
        self._graine = value

    def bloom(self) -> None:
        super().bloom()
        self._graine = self._graine + 1

    def show(self) -> None:
        super().show()
        print(f"Seed: {self._graine}")


def global_stat(plante: Plant) -> None:
    print(f"== {plante._name} Statistic ==")
    plante.stat_plant()


if __name__ == "__main__":
    print("== Garden statistics")
    print("== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_a_year(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    anonyme = Plant.anonymous()

    flower.show()
    flower.stat_plant()
    flower.bloom()
    flower.grow()
    flower.show()
    flower.stat_plant()

    print("\n=== Tree")
    oak.show()
    oak.stat_plant()
    oak.produce_shader()
    oak.stat_plant()

    print("\n=== Seed")
    seed.show()
    seed.stat_plant()
    seed.age()
    seed.grow()
    seed.bloom()
    seed.show()

    print("\n=== Anonymous")
    anonyme.show()
    anonyme.stat_plant()
