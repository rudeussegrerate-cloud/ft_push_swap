def reccurcive(n: int) -> None:
    if (n > 1):
        reccurcive(n - 1)
    print(f"Day {n}")


def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))
    reccurcive(n)
    print("Harvest time!")
