from pydantic import BaseModel

from shared_core.tools import (
    BaseTool,
    ToolResult,
)

from workspace import Workspace
from safety import SafetyValidator


workspace = Workspace()


class WriteFileArgs(BaseModel):

    path: str

    content: str


class WriteFileTool(BaseTool):

    name = "write_file"
    description = "Overwrite a text file."

    args_schema = WriteFileArgs

    def execute(
        self,
        args: WriteFileArgs,
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

        file_path.write_text(
            args.content,
            encoding="utf-8",
        )

        return ToolResult(

            success=True,

            message="File updated."

        )