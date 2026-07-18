import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.save = list[int, str]
    
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output() -> tuple[int, str]:
        pass    

class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
    
    def validate(self, data :typing.Any) -> bool:
        if (isinstance(data, int | float )):
            return True
        return False
    
    def ingest(self, data: typing.Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper numeric data")
        else:
            self.save.append(int(data))
    
    def output(self) -> tuple[int, str]:
        return (0, "ok")


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if (not isinstance(data, str)):
            raise Exception("Got exception: Improper numeric data")
        else:
            self.save.append(int(data))

class LogProcessor(DataProcessor):
    pass

if __name__ == "__main__":
    num = NumericProcessor()
    print(num.validate("s"))
