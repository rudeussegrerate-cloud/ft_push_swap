def ft_count_harvest_iterative() -> None:
    n = int(input("Days until harvest: "))
    if n == 0:
        print(f"Day {n}")
    for i in range(1, n + 1):
        print(f"Day {i}")
    print("Harvest time!")
