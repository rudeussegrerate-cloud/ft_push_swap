def test_temperature(temp:int)->int:
    try:
        temp = int(temp)
        if (temp < 0):
            raise TypeError("la temperatur est trop froid")
        if(temp > 40):
            raise TypeError("la temperatur est trop chaud")
        return (temp)
    except (TypeError, ValueError) as e:
        print(f"{e}")

def input_temperature(temp_str:str)->int:
    temp_int = test_temperature(temp_str)
    if (temp_int):
        print(f"Temperature is {temp_int}")
    return (temp_int)

def ft_raise_exception(temp:int)->None:
    test_temperature(temp)
