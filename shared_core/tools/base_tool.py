from abc import ABC
from abc import abstractmethod
from typing import Type

from pydantic import BaseModel

from .result import ToolResult
from .schemas import EmptyArgs


class BaseTool(ABC):

    name: str = ""

    description: str = ""

    args_schema: Type[BaseModel] = EmptyArgs

    result_schema: Type[BaseModel] = ToolResult

    def schema(self):

        return {

            "type": "function",

            "function": {

                "name": self.name,

                "description": self.description,

                "parameters": self.args_schema.model_json_schema(),

            },

        }

    def validate_arguments(
        self,
        arguments: dict,
    ):

        return self.args_schema.model_validate(
            arguments
        )

    @abstractmethod
    def execute(
        self,
        args: BaseModel,
    ) -> ToolResult:
        ...