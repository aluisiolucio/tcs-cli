from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_commands(self, arg: str = None) -> List[dict]:
        pass


class Context():
    def __init__(self) -> None:
        self._strategy: Strategy = None

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def commands(self, arg: str = None) -> None:
        return self._strategy.do_commands(arg)

