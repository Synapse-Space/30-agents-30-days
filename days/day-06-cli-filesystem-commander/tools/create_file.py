from pathlib import Path

from pydantic import BaseModel

from shared_core.tools import (
    BaseTool,
    ToolResult,
    ToolMetadata,
)

from workspace import Workspace
from safety import SafetyValidator


workspace = Workspace()


class CreateFileArgs(BaseModel):

    path: str

    content: str = ""


class CreateFileTool(BaseTool):

    metadata = ToolMetadata(
        name="create_file",
        description="Create a new text file.",
        category="filesystem",
    )

    args_schema = CreateFileArgs

    def execute(
        self,
        args: CreateFileArgs,
    ) -> ToolResult:

        file_path = workspace.resolve(
            args.path
        )

        SafetyValidator.validate(
            file_path
        )

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            args.content,
            encoding="utf-8",
        )

        return ToolResult(

            success=True,

            message="File created.",

            data={

                "path": str(file_path)

            }

        )