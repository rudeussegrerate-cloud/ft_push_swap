from abc import ABC, abstractmethod
from typing import Any, Protocol
import typing


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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


display_name: dict[str, str] = {
    "NumericProcessor": "Numeric Processor",
    "TextProcessor": "Text Processor",
    "LogProcessor": "Log Processor",
}


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
                print("DataStream error -", end="")
                print(f" Can't process element in stream: {data}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.save_process:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc.save:
                    break
                data.append(proc.output())
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.save_process:
            print("No processor found, no data")
            return
        for proc in self.save_process:
            class_name = type(proc).__name__
            name = display_name.get(class_name, class_name)
            print(
                f"{name}: total {proc.stat_process} items processed, "
                f"remaining {len(proc.save)} on processor"
            )


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("{" + ", ".join(pairs) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    try:
        print("Initialize Data Stream...\n")

        stream = DataStream()
        stream.print_processors_stats()
        print()

        num = NumericProcessor()
        text = TextProcessor()
        log = LogProcessor()

        print("Registering Processors\n")
        stream.register_processor(num)
        stream.register_processor(text)
        stream.register_processor(log)

        csv_plugin = CsvExportPlugin()
        json_plugin = JsonExportPlugin()

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

        print(f"Send first batch of data on stream: {batch}\n")
        stream.process_stream(batch)
        stream.print_processors_stats()
        print()

        print("Send 3 processed data from each processor to a CSV plugin:")
        stream.output_pipeline(3, csv_plugin)
        print()
        stream.print_processors_stats()
        print()

        batch = [
            21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [
                {'log_level': 'ERROR', 'log_message': '500 server crash'},
                {'log_level': 'NOTICE',
                 'log_message': 'Certificate expires in 10 days'},
            ],
            [32, 42, 64, 84, 128, 168],
            'World hello',
        ]

        print(f"Send another batch of data: {batch}\n")
        stream.process_stream(batch)
        stream.print_processors_stats()
        print()

        print("Send 5 processed data from each processor to a JSON plugin:")
        stream.output_pipeline(5, json_plugin)
        print()
        stream.print_processors_stats()
    except Exception as error:
        print(error)
