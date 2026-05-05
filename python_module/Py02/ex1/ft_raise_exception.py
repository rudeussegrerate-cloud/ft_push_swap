def test_temperature() -> None:
    test_list = ['25', 'abc', '100','-50']
    print("=== Garden Temperature ===\n")
    for test in test_list:
        print(f"input data is {test}")
        if(input_temperature(test)):
            print(f"Temperature is now {test}\n")
    print("\nAll tests completed - program didn't crash!")


def input_temperature(temp_str:str)->int:
    try:
        temp = int(temp_str)
        if (temp < 0):
            raise Exception("la temperatur est trop froid")
        if(temp > 40):
            raise Exception("la temperatur est trop chaud")
        return (temp)
    except (Exception, ValueError) as e:
        print(f"Caught input_temperature error: {e}\n")


test_temperature()