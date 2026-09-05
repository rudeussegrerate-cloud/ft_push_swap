from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.save: list[str] = []
        self.position: int = 0
        self.stat_process: int = 0

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
                self.stat_process += 1
        else:
            self.save.append(str(data))
            self.stat_process += 1


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
                self.stat_process += 1
        else:
            self.save.append(data)
            self.stat_process += 1


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
                self.stat_process += 1
        else:
            self.save.append(f"{data['log_level']}: {data['log_message']}")
            self.stat_process += 1


class DataStream:
    def __init__(self) -> None:
        self.save_process: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.save_process.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            handled = False
            for proc in self.save_process:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if not handled:
                print("DataStream error - ", end="")
                print(f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.save_process:
            print("No processor found, no data")
            return
        for proc in self.save_process:
            name = type(proc).__name__
            print(
                f"{name}: total {proc.stat_process} items processed, "
                f"remaining {len(proc.save)} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    try:
        print("Initialize Data Stream...")
        stream_processor = DataStream()
        stream_processor.print_processors_stats()
        print()

        num = NumericProcessor()
        text = TextProcessor()
        log = LogProcessor()

        print("Registering Numeric Processor\n")
        stream_processor.register_processor(num)

        batch: list[Any] = [
            'Hello world',
            [3.14, -1, 2.71],
            [
                {'log_level': 'WARNING',
                 'log_message': 'Telnet access! Use ssh instead'},
                {'log_level': 'INFO',
                 'log_message': 'User wil is connected'},
            ],
            42,
            ['Hi', 'five'],
        ]

        print(f"Send first batch of data on stream: {batch}")
        stream_processor.process_stream(batch)
        stream_processor.print_processors_stats()
        print()

        print("Registering other data processors")
        stream_processor.register_processor(text)
        stream_processor.register_processor(log)

        print("Send the same batch again")
        stream_processor.process_stream(batch)
        stream_processor.print_processors_stats()
        print()

        num_cons = 3
        text_cons = 2
        log_cons = 1

        print("Consume some elements from the data processors:", end="")
        print(f" Numeric {num_cons}, Text {text_cons}, Log {log_cons}")
        try:
            for _ in range(num_cons):
                num.output()
            for _ in range(text_cons):
                text.output()
            for _ in range(log_cons):
                log.output()
        except Exception:
            pass

        stream_processor.print_processors_stats()
    except Exception as error:
        print(error)
