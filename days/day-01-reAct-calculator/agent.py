from shared_core.llm_client import LLMClient
from shared_core.logger import logger
from shared_core.prompts.react import SYSTEM_PROMPT

from parser import ReActParser
from tools import calculator

class ReActAgent:
    def __init__(self):
        self.llm=LLMClient()
        self.messages=[{
            "role":"system",
            "content":SYSTEM_PROMPT
        }]
        self.tools={
            "calculator":calculator
        }

    def run(self, user_query:str):
        self.messages.append({
            "role":"user",
            "content":user_query
        })

        max_iterations=5

        for step in range(max_iterations):
            logger.info("="*70)
            logger.info(f"Iteration {step+1}")

            reply=self.llm.invoke(self.messages)
            logger.info("\nLLM RESPONSE\n%s",reply)

            self.messages.append({
                "role":"assistant",
                "content":reply
            })

            parsed=ReActParser.parse(reply)

            if parsed.thought:

                print("\n Thought")
                print("-"*30)
                print(parsed.thought)
            
            if parsed.final_answer:
                print("\n FINAL ANSWER")
                print("-"*30)
                print(parsed.final_answer)
                return parsed.final_answer

            if not parsed.action:
                print("\nNo action returned by model.")
                return None

            tool=self.tools.get(parsed.action)

            if tool is None:
                observation=f"Unknown Tool '{parsed.action}'"
            
            else:
                observation =tool(parsed.action_input)

            print("\nAction")
            print("-"*30)
            print(parsed.action)

            print("\nAction Input")
            print("-"*30)
            print(parsed.action_input)

            self.messages.append({
                "role":"user",
                "content":f"Observation: {observation}"
            })
        print("\nMaximum iterations reached.")

        return None
    