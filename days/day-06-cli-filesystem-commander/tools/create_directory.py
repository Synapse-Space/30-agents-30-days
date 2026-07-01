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


class CreateDirectoryArgs(BaseModel):

    path: str


class CreateDirectoryTool(BaseTool):

    metadata = ToolMetadata(
        name="create_directory",
        description="Create a new directory.",
        category="filesystem",
    )

    args_schema = CreateDirectoryArgs

    def execute(
        self,
        args: CreateDirectoryArgs,
    ) -> ToolResult:

        dir_path = workspace.resolve(
            args.path
        )

        SafetyValidator.validate(
            dir_path
        )

        dir_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return ToolResult(

            success=True,

            message="Directory created."

        )