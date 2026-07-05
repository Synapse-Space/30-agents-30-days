from shared_core.agents import MemoryAgent
from memory_extractor import MemoryExtractor
from prompts import SYSTEM_PROMPT

class MemoryChatbot(MemoryAgent):
    def __init__(self,memory_manager,llm):
        super().__init__(SYSTEM_PROMPT,memory_manager)

        self.extractor=(MemoryExtractor(llm))

    def chat(self, user_id:str,message:str):
        memories=self.memory.recall(user_id)
        context=""
        if memories:
            context="\nKnown Facts:\n"
            for key,value in memories.items():
                context+=f"-{key}:{value}\n"
        
        prompt = f"""

Known Memories

{context}

User:

{message}
"""
        
         result=self.extractor.extract(prompt)
         if result.should_remember:
            self.memory.remember(user_id,result.key, result.value)

        
        return result.response
