from typing import Any


def config(conf: list[tuple[str, str]]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    pos: list[int] = []
    for _, elem in conf:
        elems = elem.split()
        for integ in elems:
            try:
                pos.append(int(integ))
            except ValueError:
                continue
        result.append((pos[0], pos[1]))
        pos.pop(1)
        pos.pop(0)

    return result


def zone_name(config: list[tuple[str, str]]) -> list[str]:
    result: list[str] = []
    for _, elem in config:
        elem = elem.split()
        result.append(elem[0])

    return result


def metadata(config: list[tuple[str, str]]) -> list[str]:
    result: list[str] = []
    start = 0
    end = 0
    for _, elem in config:
        new_elem = elem.strip()
        for char in new_elem[:]:
            if char == "[":
                start += 1
                break
            start += 1
        for char1 in new_elem[:]:
            if char1 == "]":
                break
            end += 1
        res = new_elem[start:end]
        result.append(res)
        start = 0
        end = 0

    return result


with open("maps/medium/03_priority_puzzle.txt", 'r') as f:
    textes = f.readlines()
    lis: list[str] = []
    result: list[Any] = []
    for text in textes:
        if text.startswith("#") or text == "\n":
            continue
        else:
            lis.append(text.strip())
    for tup in lis:
        result.append(tuple(tup.split(":")))
# print(result)
start: list[tuple[str, str]] = []
hub: list[tuple[str, str]] = []
end: list[tuple[str, str]] = []
nbr_drone: list[tuple[str, str]] = []
connection: list[list[str, str]] = []

for key, value in result:
    if "nb_drones" == key:
        nbr_drone.append((key, value))
    if "end_hub" == key:
        end.append((key, value))
    if "start_hub" == key:
        start.append((key, value))
    if "hub" == key:
        hub.append((key, value))
    if "connection" == key:
        connection.append((key, value))
while result:
    result.pop(0)

coord_start = config(start)
coord_hub = config(hub)
coord_end = config(end)

print(coord_start)
print(coord_hub)
print(coord_end)
print()


print(zone_name(start))
print(zone_name(hub))
print(zone_name(end))
print()

print(metadata(start))
print(metadata(hub))
print(metadata(end))
print()

print(connection)