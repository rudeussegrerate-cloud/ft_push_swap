from .. import potions, elements
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: "
            f"brew ’{elements.create_air()}’ and ’{potions.strength_potion()}’"
            f"mixed with ’{create_fire()}’"
            )
