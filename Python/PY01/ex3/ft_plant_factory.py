#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, p_age: int):
        self.name = name
        self.height = float(height)
        self.p_age = p_age
        self.up_grow = 0.4

    def grow(self) -> None:
        if self.name == "Rose":
            self.up_grow = 0.8
        elif self.name == "Sunflower":
            self.up_grow = 0.5
        elif self.name == "Cactus":
            self.up_grow = 0.2
        self.height = round(self.height + self.up_grow, 1)

    def age(self) -> None:
        self.p_age = self.p_age + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")


def ft_plant_factory() -> None:
    plante = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 20, 65),
              Plant("Fern", 15, 120)]

    for i in range(5):
        print("created: ", end="")
        plante[i].show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
