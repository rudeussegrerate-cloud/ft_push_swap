import abc
import typing
import builtins


class DataProcessor(abc.ABCMeta):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    pass

class TextProcessor(DataProcessor):
    pass

class LogProcessor(DataProcessor):
    pass

