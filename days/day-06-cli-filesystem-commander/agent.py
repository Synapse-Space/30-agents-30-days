
from shared_core.agents import ToolAgent
from shared_core.llms import LLMFactory

from tools.create_file import CreateFileTool
from tools.read_file import ReadFileTool
from tools.write_file import WriteFileTool
from tools.delete_file import DeleteFileTool
from tools.create_directory import CreateDirectoryTool
from tools.list_directory import ListDirectoryTool

SYSTEM_PROMPT = """
You are a filesystem assistant.

Your job is to:

1. Understand the user's request.

2. Choose the correct tool.

3. Explain what you are about to do.

4. Never execute dangerous operations.

5. Stay inside the workspace.

Always call one tool.

Never invent results.
"""


class FileSystemAgent(ToolAgent):

    def __init__(self):

        super().__init__(
            system_prompt=SYSTEM_PROMPT
        )

        self.add_tool(CreateFileTool())
        self.add_tool(ReadFileTool())
        self.add_tool(WriteFileTool())
        self.add_tool(DeleteFileTool())
        self.add_tool(CreateDirectoryTool())
        self.add_tool(ListDirectoryTool())