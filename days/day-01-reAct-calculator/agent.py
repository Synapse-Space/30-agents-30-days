from shared_core.agents import BaseAgent
from shared_core.prompts.react import SYSTEM_PROMPT

from parser import ReActParser
from tools import calculator

class ReActAgent(BaseAgent):
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
        self.tools={
            "calculator":calculator
        }

    def run(self, user_query:str):
        self.add_user_message(user_query)

        max_iterations=5

        for step in range(max_iterations):
            self.logger.info("="*70)
            self.logger.info(f"Iteration {step+1}")

            response=self.chat()
            reply=response["message"]["content"]
            self.logger.info("\nLLM RESPONSE\n%s",reply)

            self.add_assistant_message(reply)

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

            self.add_user_message(f"Observation: {observation}")
        print("\nMaximum iterations reached.")

        return None
    