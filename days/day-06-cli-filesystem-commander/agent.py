
from shared_core.agents import ToolAgent
from shared_core.providers.llm import LLMFactory

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

        self.register_tool(CreateFileTool())
        self.register_tool(ReadFileTool())
        self.register_tool(WriteFileTool())
        self.register_tool(DeleteFileTool())
        self.register_tool(CreateDirectoryTool())
        self.register_tool(ListDirectoryTool())