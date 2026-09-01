from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.save: list[Any] = []
        self.position: int = 0
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        element: tuple[int, str] = ()
        element = self.save.pop(0)
        p = int(self.position)
        self.position += 1
        return tuple((p, element))


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, int | float )):
            return True
        if (isinstance(data, list)):
            for element in data:
                if not isinstance(element, int | float):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper numeric data")
        else:
            self.save.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True
        if (isinstance(data, list)):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        return False


    def ingest(self, data: Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper string data")
        if (isinstance(data, list)):
            for element in data:
                if not isinstance(element, str):
                    raise Exception("Got exception: Improper string data")
                else:
                    self.save.append(str(data))
        else:
            self.save.append(str(data))




class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return True
        if (isinstance(data, list)):
            for _ in data:
                if (not isinstance(_, dict)):
                    return False
            return True
        return False


    def ingest(self, data: Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper dict data")
        if (isinstance(data, list)):
            for element in data:
                if not isinstance(element, dict):
                    raise Exception("Got exception: Improper dict data")
                else:
                    self.save.append(str(data))           
        else:
            self.save.append(str(data))



if __name__ == "__main__":
    try:
        num = NumericProcessor()
        text = TextProcessor()
        log = LogProcessor()
        data: list[Any] = []
        value_extract = 3

        data = [1, 2, 3, 4, 5]
        print("=== Code Nexus - Data Processor ===")
        print("Testing Numeric Processor...")
        print(f"Trying to validate input '42': {num.validate(42)}")
        print(f"Trying to validate input 'Hello': {num.validate('Hello')}")
        print("Test invalid ingestion of string 'foo' without prior validation:")

        try:
            num.ingest('foo')
        except Exception as e:
            print(e)

        print(f"Processing data: {data}")

        for d in data:
            num.ingest(d)

        print(f"Extracting 3 values...")
        for _ in range(3):
            a = num.output()
            print(f"Numeric value {a[0]}: {a[1]}")

        print("Testing Text Processor...")
        print(f"Trying to validate input '42': {text.validate(42)}")
        data = ['Hello', 'Nexus', 'World']

        for value in data:
            text.ingest(value)


        for i in range(2):
            a = text.output()
            print(f"Text value {a[0]}: {a[1]}")


        print("Testing Log Processor...")
        print(f"Trying to validate input '42': {log.validate(42)}")
        data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]

        print(f"Processing data: {data}\n")
        print("Extracting 2 values...")

        for value in data:
            log.ingest(value)

        a: tuple[int, str]= []
        for _ in range(5):
            i,a = log.output()
            print(f"Log entry {i}: {a}")
    except Exception as error:
        print(f"error: {error}")

