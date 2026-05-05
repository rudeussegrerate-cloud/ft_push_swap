def test_temperature() -> None:
    test_list = ['25', 'abc']
    print("=== Garden Temperature ===")
    for test in test_list:
        print(f"input data is {test}")
        if(input_temperature(test)):
            print(f"Temperature is now {test}\n")
    print("\nAll tests completed - program didn't crash!")


def input_temperature(temp_str: str) -> int:
    try:
        stemp = int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        stemp = 0
    return (stemp)

if __name__ == "__main__":
    test_temperature()