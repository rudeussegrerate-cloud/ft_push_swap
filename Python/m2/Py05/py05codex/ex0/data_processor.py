from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.save: list[str] = []
        self.position: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.save) == 0:
            raise Exception("no one else item to pop:p")
        element = self.save.pop(0)
        rank = self.position
        self.position += 1
        return (rank, element)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if isinstance(data, list):
            for element in data:
                self.save.append(str(element))
        else:
            self.save.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper string data")
        if isinstance(data, list):
            for element in data:
                self.save.append(element)
        else:
            self.save.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper dict data")
        if isinstance(data, list):
            for element in data:
                self.save.append(
                    f"{element['log_level']}: {element['log_message']}"
                )
        else:
            self.save.append(f"{data['log_level']}: {data['log_message']}")


if __name__ == "__main__":
    try:
        num = NumericProcessor()
        text = TextProcessor()
        log = LogProcessor()

        print("=== Code Nexus - Data Processor ===\n")

        print("Testing Numeric Processor...")
        print(f"Trying to validate input '42': {num.validate(42)}")
        print("Test invalid ingestion of", end="")
        print(" string 'foo' without prior validation:")

        numeric_data: list[int | float] = [1, 2, 3, 4, 5]
        print(f"Processing data: {numeric_data}")
        for num_item in numeric_data:
            num.ingest(num_item)

        print("Extracting 3 values...")
        for _ in range(3):
            num_rank, num_value = num.output()
            print(f"Numeric value {num_rank}: {num_value}")
        print()

        print("Testing Text Processor...")
        text_data: list[str] = ['Hello', 'Nexus', 'World']
        print(f"Processing data: {text_data}")
        for text_item in text_data:
            text.ingest(text_item)

        print("Extracting 1 value...")
        text_rank, text_value = text.output()
        print(f"Text value {text_rank}: {text_value}")
        print()

        print("Testing Log Processor...")
        print("Test invalid ingestion of", end="")
        print(" str 'Hello' without prior validation:")
        try:
            log.ingest("Hello")
        except Exception as e:
            print(e)

        log_data: list[dict[str, str]] = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
        ]
        print(f"Processing data: {log_data}\n")
        for log_item in log_data:
            log.ingest(log_item)

        print("Extracting 2 values...")
        for _ in range(2):
            log_rank, log_value = log.output()
            print(f"Log entry {log_rank}: {log_value}")

    except Exception as error:
        print(f"error: {error}")
