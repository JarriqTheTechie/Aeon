import json
import threading
from typing import Any, Protocol


class BackgroundTaskInterface(Protocol):
    @classmethod
    def fire(self, function: callable, args: Any = None) -> Any:
        raise NotImplementedError()

    @classmethod
    def _function_wrapper(cls, function: callable, args: Any) -> None:
        raise NotImplementedError()


class BackgroundTask(BackgroundTaskInterface):
    @classmethod
    def fire(cls, function: callable, args: Any = None):
        threading.Thread(target=cls._function_wrapper, args=(function, args)).start()

    @classmethod
    def _function_wrapper(cls, function: callable, args: Any):
        function(args)
        print("Fire and Forget ran. \n")



