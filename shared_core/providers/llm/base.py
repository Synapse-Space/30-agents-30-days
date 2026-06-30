from abc import ABC
from abc import abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def chat(
        self,
        messages,
        tools=None,
        format=None,
    ):
        ...

    @abstractmethod
    def structured(
        self,
        messages,
        schema,
    ):
        ...