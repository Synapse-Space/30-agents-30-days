from pathlib import Path
from pydantic import BaseModel
from shared_core.tools import BaseTool, ToolResult
from workspace import Workspace
from safety import SafetyValidator

workspace = Workspace()

class DeleteFileArgs(BaseModel):
    path: str

class DeleteFileTool(BaseTool):
    name = "delete_file"
    description = "Delete a file."
    
    args_schema = DeleteFileArgs
    
    def execute(self, args: DeleteFileArgs) -> ToolResult:
        file_path = workspace.resolve(args.path)
        SafetyValidator.validate(file_path)
        
        if not file_path.exists():
            return ToolResult(success=False, message="File not found.")
            
        file_path.unlink()
        return ToolResult(success=True, message="File deleted.")
