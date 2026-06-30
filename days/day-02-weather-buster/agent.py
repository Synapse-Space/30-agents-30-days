import json

from shared_core.agents import BaseAgent
from shared_core.tools.registry import tool_registry
from tool_schema import WEATHER_TOOL
from weather_api import WeatherAPI
from shared_core.prompts.weather import SYSTEM_PROMPT

class WeatherAgent(BaseAgent):

    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
        self.registry=tool_registry
        self.registry.register("get_weather",WeatherAPI.get_weather)

    def run(self, query:str):
        self.add_user_message(query)

        response=self.chat(tools=[WEATHER_TOOL])

        assistant=response["message"]
        self.add_assistant_message(assistant.get("content") or "")

        if assistant.get("tool_calls"):
            self.logger.info("tool call detected.")

            for tool_call in assistant["tool_calls"]:
                function=tool_call["function"]
                tool_name=function["name"]
                arguments=function["arguments"]

                self.logger.info(
                    "executing tool %s with args %s",
                    tool_name,
                    arguments
                )

                result=self.registry.execute(tool_name,**arguments)

                self.logger.info(result)

                self.add_tool_message(tool_name, json.dumps(result))

            final=self.chat()
            final_message=final["message"]["content"]
            self.add_assistant_message(final_message)
            return final_message

        return assistant["content"]
