from shared_core.agents.base_agent import BaseAgent 
from shared_core.tools.result import ToolResult
from shared_core.tools.executor import ToolExecutor
from shared_core.tools.registry import ToolRegistry

class ToolAgent(BaseAgent):
    def __init__(self, system_prompt:str):
        super().__init__(system_prompt)
        self.registry=ToolRegistry()
        self.executor=ToolExecutor(self.registry)

        
    def register_tool(self,tool):
        self.registry.register(tool)

    def available_tools(self):
        return self.registry.schemas()

    def run(self, user_input: str, max_steps: int = 5):
        self.clear_history()
        self.add_user_message(user_input)

        for _ in range(max_steps):
            response = self.chat(tools=self.available_tools())
            message = response.get("message", {})

            # Append the assistant's message (which includes tool_calls)
            self.messages.append(message)

            if "tool_calls" not in message or not message["tool_calls"]:
                return message.get("content", "")

            for tool_call in message["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                arguments = tool_call["function"]["arguments"]

                try:
                    tool_result = self.executor.execute(tool_name, arguments)
                    result_str = str(tool_result.data) if tool_result.success else str(tool_result.message)
                except Exception as e:
                    result_str = f"Error: {e}"

                self.add_tool_message(tool_name, result_str)

        return "Agent stopped after reaching maximum steps."
