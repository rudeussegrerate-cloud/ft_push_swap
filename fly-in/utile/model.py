from abc import ABC, abstractmethod


class Zone(ABC):
    def __init__(self, cost: int = 1, capacity: int = 1):
        self._cost = cost
        self._capacity = capacity

    @abstractmethod
    def isopen(self) -> bool:
        pass


    @abstractmethod
    def cost(self):
        return self._cost


    @abstractmethod
    def tour_estimation():
        pass


