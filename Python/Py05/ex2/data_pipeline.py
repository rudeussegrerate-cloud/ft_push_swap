from abc import ABC, abstractmethod
from typing import Any, Protocol
import typing

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass



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
        print("Registering Processors")
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


    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        try:
            for proc in self.save_process:
                data: list[int, str] = []
                for _ in range(nb):
                    data.append(proc.output())
                if data is not None:
                    plugin.process_output(data)
        except Exception as e:
            print("\nGot error", e)


    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.save_process) == 0:
            print("No processor found, no data")
        else:
            for stat in self.save_process:
                print(f"{type(stat).__name__}: total {stat.stat_process} items processed, remaining {len(stat.save)} on processor")


class Csvexportplugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print(f"===This is an CsvExportPlugin ===")
        for element in data:
            print(element[1], end="")
        print()

class Jsonexportplugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print(f"===This is an JsonExportPlugin ===")
        for element in data:
            print('{"item', element[0],'"', ':','"',element[1],'"}, ', end="")
        print()



if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)
    csv = Csvexportplugin()

    batch = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
            'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]


    stream.process_stream(batch)
    stream.print_processors_stats()
    stream.output_pipeline(2, csv)

    stream.print_processors_stats()
    batch =  [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
             [{'log_level': 'ERROR', 'log_message': '500 server crash'},
              {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
             [32, 42, 64, 84, 128, 168], 'World hello']
    
    print("Send another batch of data: ", batch)
    stream.process_stream(batch)
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(2, Jsonexportplugin())

    stream.print_processors_stats()
