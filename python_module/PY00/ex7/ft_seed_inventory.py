def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit.capitalize() == "packets".capitalize()):
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif (unit.capitalize() == "grams".capitalize()):
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif (unit.capitalize() == "area".capitalize()):
        print(f"{seed_type.capitalize()} seeds: ", end="")
        print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
