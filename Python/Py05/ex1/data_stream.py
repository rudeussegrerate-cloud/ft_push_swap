from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.save: list[Any] = []
        self.position: int = 0
        self.stat_process = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        self.stat_process += 1

    def output(self) -> tuple[int, str]:
        element = self.save.pop(0)
        p = int(self.position)
        self.position += 1
        return tuple(p, element)


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
        if (isinstance(data, list)):
            for element in data:
                self.save.append(str(element))
                self.stat_process += 1
        else:
            self.save.append(str(data))
            self.stat_process += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
            super().__init__()

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
                self.save.append(str(element))
                self.stat_process += 1
        else:
            self.save.append(str(data))
            self.stat_process += 1



class LogProcessor(DataProcessor):
    def __init__(self) -> None:
            super().__init__()
    def validate(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return True
        if (isinstance(data, list)):
            for element in data:
                if not isinstance(element, dict):
                    return False
            return True
        return False


    def ingest(self, data: Any) -> None:
        if (not self.validate(data)):
            raise Exception("Got exception: Improper dict data")
        if (isinstance(data, list)):
            for element in data:
                self.save.append(str(element))
                self.stat_process += 1
        else:
            self.save.append(str(data))
            self.stat_process += 1

class DataStream:

    def __init__(self):
        self.save_process: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.save_process.append(proc)


    def process_stream(self, stream: list[typing.Any]) -> None:
        who_can = 0
        for pr_data in self.save_process:
            no = 0
            for data in stream:
                try:
                    if not pr_data.validate(data):
                        no = 1
                        raise Exception(f"DataStream error - Can't process element in stream: {data}")
                    pr_data.ingest(data)
                except Exception as error:
                    print(error)

            if not no:
                who_can += 1
                print("ok")


    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        for stat in self.save_process:
            print(f"{type(stat).__name__}: total {stat.stat_process} items processed, remaining {len(stat.save)} on processor")


if __name__ == "__main__":

    print("=== Code Nexus - Data Stream ===")
    process = DataStream()
    print("Initialize Data Stream...")
    if (not process.save_process):
        print("No processor found, no data\n")
    
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("Registering Numeric Processor\n")
    process.register_processor(num)
    batch = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
            'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]

    try:
        print(f"Send first batch of data on stream:{batch}")
        process.process_stream(batch)
    except Exception as error:
        print(error)

    process.print_processors_stats()
    print("Registering other data processors")
    process.register_processor(text)
    process.register_processor(log)

    try:
        print("Send the same batch again")
        process.process_stream(batch)
    except Exception as error:
        print(error)

    
    print("Consume some elements from the data processors")

    try:
        for i in range(3):
            for j in range(2):
                process.save_process[i].output()
    except (Exception, IndexError) as error:
        print(error)

    process.print_processors_stats()


