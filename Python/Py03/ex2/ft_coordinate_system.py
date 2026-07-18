#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, ...]:
    while (1):
        try:
            coordtmp = [float()] * 3
            coordinate = input("Enter new coordinates as floats"
                               " in format 'x,y,z': ").split(',')
            i = 0
            for _ in coordinate:
                i += 1
            if (i != 3):
                print("Invalid Syntax!")
                continue
            i = 0
            while (i < 3):
                coordtmp[i] = float(coordinate[i])
                i += 1
            if (len(coordinate) == 3):
                break
        except (ValueError) as e:
            print(f"Error on parameter '{coordinate[i]}': {e}")
    return tuple(coordtmp)


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        print("Get a first set of coordinates")
        a = get_player_pos()
        print("Got a first tuple:", a)
        print(f"It includes: X={a[0]}, Y={a[1]}, Z={a[2]}")
        distance = math.sqrt((a[0]-0)**2 + (a[1]-0)**2 + (a[2]-0)**2)
        print(f"Distance to center: {round(distance, 4)}\n")
        print("Get a second set of coordinates")
        b = get_player_pos()
        distance = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)
        print("Distance between the 2 sets", end="")
        print(f"of coordinates: {round(distance, 4)}")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting programme;)")
