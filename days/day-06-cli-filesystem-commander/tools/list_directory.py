from pathlib import Path
from pydantic import BaseModel
from shared_core.tools import BaseTool, ToolResult
from workspace import Workspace
from safety import SafetyValidator

workspace = Workspace()

class ListDirectoryArgs(BaseModel):
    path: str

class ListDirectoryTool(BaseTool):
    name = "list_directory"
    description = "List contents of a directory."
    
    args_schema = ListDirectoryArgs
    
    def execute(self, args: ListDirectoryArgs) -> ToolResult:
        dir_path = workspace.resolve(args.path)
        SafetyValidator.validate(dir_path)
        
        if not dir_path.exists():
            return ToolResult(success=False, message="Directory not found.")
            
        if not dir_path.is_dir():
            return ToolResult(success=False, message="Path is not a directory.")
            
        contents = [p.name for p in dir_path.iterdir()]
        return ToolResult(success=True, message="Directory listed.", data={"contents": contents})
