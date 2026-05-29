import math


def get_player_pos() -> tuple[float, ...]:
    while (1):
        try:
            coordtmp = [float(0)] * 3
            coordinate = input("Enter new coordinates as floats"
                               " in format 'x,y,z': ").split(',', 3)
            i = 0
            while (i < 3):
                coordtmp[i] = float(coordinate[i])
                i += 1
            if (len(coordinate) == 3):
                break
        except Exception as e:
            print(f"invalid syntax: {e}")
    return tuple(coordtmp)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    a = get_player_pos()
    print("Got a first tuple:", a)
    print(f"It includes: X={a[0]}, Y={a[1]}, Z={a[2]}")
    distance = math.sqrt((a[0]-0)**2 + (a[1]-0)**2 + (a[2]-0)**2)
    print(f"Distance to center: {round(distance, 4)}\n")
    print("Get a second set of coordinates")
    b = get_player_pos()
    print("Got a first tuple:", a)
    print(f"It includes: X={b[0]}, Y={b[1]}, Z={b[2]}")
    distance = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)
    print("Distance to center: ", round(distance, 4))
