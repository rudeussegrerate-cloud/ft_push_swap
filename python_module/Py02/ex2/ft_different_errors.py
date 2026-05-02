def operation_set(operation):
    if (operation == 0):
        value = "abc"
        value = int(value)
    elif (operation == 1):
        value = 10
        value = value/0
    elif (operation == 2):
        with open('fichier_inexistant.txt', 'r') as file:
            value = file.read()
    elif(operation == 3):
        Value = "Sdsfoije" + 12
    else:
        print("successfuly operation number set ;)")


def test_error_types(Value:int)->int:
    try:
        operation_set(Value)
        return (Value)

    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught TypeError: {e}")
        return (0)

def garden_operations(operation_number:int)->int:
    if (test_error_types(operation_number)):
        return (operation_number)
    return (-1) #irreur signification !
