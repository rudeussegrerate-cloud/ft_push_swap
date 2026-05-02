def test_temperature(temp: str) -> int:
    try:
        stemp = int(temp)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        stemp = 0
    return (stemp)

def input_temperature(temp_str: str) -> int:
    temp_int = test_temperature(temp_str)
    return (temp_int)