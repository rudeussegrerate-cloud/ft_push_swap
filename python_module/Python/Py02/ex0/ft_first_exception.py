def test_temperature() -> None:
    test_list = ['25', 'abc']
    data = 0
    for test in test_list:
        print(f"input data is {test}")
        try:
            print(input_temperature(test))
            data = input_temperature(test)
            print(f"Temperature is now {data}\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


def input_temperature(temp_str: str) -> int:
    stemp = int(temp_str)
    return (stemp)


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
