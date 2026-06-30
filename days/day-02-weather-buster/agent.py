import json

from shared_core.logger import logger
from shared_core.llm_client import LLMClient
from shared_core.tools.registry import tool_registry
from tool_schema import WEATHER_TOOL
from weather_api import WeatherAPI
from shared_core.prompts.weather import SYSTEM_PROMPT

class WeatherAgent:

    def __init__(self):
        self.llm=LLMClient()
        self.registry=tool_registry

        self.registry.register("get_weather",WeatherAPI.get_weather)
        self.messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT,
            }
        ]
    
    def chat( self,query:str):
        self.messages.append({
            "role":"user",
            "content":query
        })

        response=self.llm.chat(
            messages=self.messages,
            tools=[WEATHER_TOOL]
        )

        assistant=response["message"]
        self.messages.append(assistant)

        if assistant.get("tool_calls"):
            logger.info("tool call detected.")

            for tool_call in assistant["tool_calls"]:
                function=tool_call["function"]
                tool_name=function["name"]
                arguments=function["arguments"]

                logger.info(
                    "executing tool %s with args %s",
                    tool_name,
                    arguments
                )

                result=self.registry.execute(tool_name,**arguments)

                logger.info(result)

                self.messages.append({
                    "role":"tool",
                    "name":tool_name,
                    "content":json.dumps(result),
                })

            final =self.llm.chat(self.messages)

            final_message=final["message"]["content"]

            self.messages.append(
                {
                    "role":"assistant",
                    "content":final_message,
                }
            )
            return final_message
        
        return assistant["content"]