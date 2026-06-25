def garden_operations(operation_number: int) -> int:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        10/0
    elif (operation_number == 2):
        with open('fichier_inexistant.txt', 'r') as file:
            file.read()
    elif (operation_number == 3):
        "Sdsfoije" + 12
    else:
        print("successfuly operation number set ;)")
    return (operation_number)


def test_error_types() -> None:
    print('=== Garden Error Types Demo ===')
    test = [0, 1, 2, 3, 4]
    for i in test:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
