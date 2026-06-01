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
                if arg[0] not in d.keys():
                    d.update({arg[0] : int(arg[1])})
            except (IndexError, ValueError) as e:
                if (IndexError):
                    print(f"NO value provided with: '{arg[0]}'")
                elif(ValueError):
                    print(f"Error qantity: '{e}'")
            i += 1
        print("Got inventory:", d)
        print(f"Item list: {list(d.keys())}")
        print(f"Total quantity of the {len(d)} items: {sum(d.values())}")
        for key in d.keys():
            print(f"Item {key} represents {round((d[key]/sum(d.values)) * 100, 1)}%")
        arg = list(d.keys())
        i = 0
        j = 0
        max = d[arg[0]]
        value = 0
        while (i < len(arg)):
            j = i + 1
            while(j < len(arg)):
                if(max < d[arg[j]]):
                    max = d[arg[j]]
                    value = j
                j+=1
            i+=1
        print(f"Item most abundant: {arg[value]} with quantity {max}")
        i = 0
        min = d[arg[0]]
        while (i < len(arg)):
            j = i + 1
            while(j < len(arg)):
                if(min > d[arg[j]]):
                    min = d[arg[j]]
                    value = j
                j+=1
            i+=1
        print(f"Item lesat abundant: {arg[value]} with quantity {min}")

        d.update({'magic_item': 1})

        print(f"Updated inventory: {d}")
