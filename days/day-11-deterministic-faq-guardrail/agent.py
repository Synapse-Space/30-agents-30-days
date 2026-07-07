import json
from pathlib import Path 
from shared_core.agents import GuardrailAgent
from faq_engine import FAQEngine 
from prompts import SYSTEM_PROMPT

class FAQGuardrailAgent(GuardrailAgent):
    def __init__(self, memory_manager):
        super().__init__(SYSTEM_PROMPT,memory_manager)
        self.engine =FAQEngine()

        self.log_file=Path("unknown_questions.json")

        if not self.log_file.exists():
            self.log_file.write_text("[]")
    
    def log_unknown(self,question:str):
        data=json.loads(self.log_file.read_text())

        data.append({
            "question":question
        })

        self.log_file.write_text(
            json.dumps(data,indent=4)
        )

    def chat(self, user_input:str):
        result=self.engine.answer(user_input)

        if result.matched:
            return {
                "source":"FAQ",
                "response":result.message
            }
        
        self._log_unknown(user_input)
        llm_response=self.generate_from_llm(user_input)

        return {
            "source":"LLM",
            "response":llm_response
        }
        