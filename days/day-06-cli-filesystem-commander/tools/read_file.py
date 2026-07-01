from pydantic import BaseModel

from shared_core.tools import (
    BaseTool,
    ToolResult,
)

from workspace import Workspace
from safety import SafetyValidator


workspace = Workspace()


class ReadFileArgs(BaseModel):

    path: str


class ReadFileTool(BaseTool):

    name = "read_file"
    description = "Read a text file."

    args_schema = ReadFileArgs

    def execute(
        self,
        args: ReadFileArgs,
    ) -> ToolResult:

        file_path = workspace.resolve(
            args.path
        )

        SafetyValidator.validate(
            file_path
        )

        if not file_path.exists():

            return ToolResult(

                success=False,

                message="File not found."

            )

        return ToolResult(

            success=True,

            message="File read.",

            data={

                "content": file_path.read_text(
                    encoding="utf-8"
                )

            }

        )