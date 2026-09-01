def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit.lower() == "packets"):
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif (unit.lower() == "grams"):
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif (unit.lower() == "area"):
        print(f"{seed_type.capitalize()} seeds: "
              f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
