#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plante1 = Plant("Rose", 25, 30)
plante2 = Plant("Sunflower", 80, 45)
plante3 = Plant("Cactus", 15, 120)


def ft_garden_data() -> None:
    plante1.show()
    plante2.show()
    plante3.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
