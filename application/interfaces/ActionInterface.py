from abc import ABC, abstractmethod
from typing import Protocol


class ActionInterface(ABC):
    @abstractmethod
    def handle(cls, *args, **kwargs) -> None:
        return

    @abstractmethod
    def as_controller(cls, *args, **kwargs) -> None:
        return

