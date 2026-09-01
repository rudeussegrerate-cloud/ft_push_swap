#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if (len(sys.argv) < 2):
        print("Error argument: more than 2 argument needed")
    else:
        i = 1
        d = {}
        while (i < len(sys.argv)):
            try:
                arg = sys.argv[i].split(":", 1)
                if not arg[0]:
                    raise IndexError()
                if arg[0] not in d:
                    if (int(arg[1]) > 0):
                        d.update({arg[0]: int(arg[1])})
                else:
                    print(f"Redundant item '{arg[0]}' - discarding")

            except IndexError:
                print(f"Error - invalid parameter : '{arg[0]}'")
            except ValueError as e:
                print(f"Quantity error for '{arg[0]}': '{e}'")
            i += 1
        print("Got inventory:", d)
        print(f"Item list: {list(d.keys())}")
        print(f"Total quantity of the {len(d)} items: {sum(d.values())}")
        for key in d.keys():
            try:
                print(f"Item {key} represents ", end="")
                print(f"{round((d[key]/sum(d.values())) * 100, 1)}%")
            except ZeroDivisionError as e:
                print(f"Error :{e}")
        arg = list(d.keys())
        i = 0
        j = 0
        try:
            max = d[arg[0]]
            value = 0
            while (i < len(arg)):
                j = i + 1
                while (j < len(arg)):
                    if (max < d[arg[j]]):
                        max = d[arg[j]]
                        value = j
                    j += 1
                i += 1
            print(f"Item most abundant: {arg[value]} with quantity {max}")
            i = 0
            j = 0
            min = d[arg[0]]
            value = 0
            while (i < len(arg)):
                j = i + 1
                while (j < len(arg)):
                    if (min > d[arg[j]]):
                        min = d[arg[j]]
                        value = j
                    j += 1
                i += 1
            print(f"Item least abundant: {arg[value]} with quantity {min}")
            d.update({'magic_item': 1})

            print(f"Updated inventory: {d}")
        except IndexError:
            print("No quantity or key provided")
