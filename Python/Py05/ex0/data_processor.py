from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.save: list[Any] = []
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return tuple((i, self.save.pop(0)) for i in range(len(self.save)))



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
                    self.save.append(data)
        else:
            self.save.append(data)




class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return True
        return False


    def ingest(self, data: Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper dict data")
        if (isinstance(data, dict)):
            for element in data:
                if not isinstance(element, str | int | float | list | dict):
                    raise Exception("Got exception: Improper dict data")
                else:
                    self.save.append(str(data))
        else:
            self.save.append(str(data))



if __name__ == "__main__":
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data = [1, 2, 3, 4, 5]
    value_extract = 3

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
    
    print(f"Extracting {value_extract} values...")    
    extract = num.output()
    extract = list(extract)
    for i in extract:
        print(f"Numeric value {i[0]}:{i[1]}")
