#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise Exception("la temperatur est trop froid")
    if (temp > 40):
        raise Exception("la temperatur est trop chaud")
    return (temp)


def test_temperature() -> None:
    test_list = ['25', 'abc', '100', '-50']
    data = 0
    print("=== Garden Temperature ===\n")
    for test in test_list:
        print(f"input data is {test}")
        try:
            data = input_temperature(test)
            print(f"Temperature is now {data}\n")
        except Exception as e:
            print(f"Caught input_temperature erro: {e}\n")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
