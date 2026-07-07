from shared_core.agents import KnowledgeAgent

from prompts import SYSTEM_PROMPT


class ContextualDocumentAgent(KnowledgeAgent):

    def __init__(

        self,

        memory_manager,

    ):

        super().__init__(

            SYSTEM_PROMPT,

            memory_manager,

        )

    def ask(

        self,

        question: str,

    ):

        results = self.search(question)

        if not results:

            return {

                "context": "",

                "response": "I couldn't find that information in the provided documents."

            }

        context = "\n\n".join(

            result.chunk.text

            for result in results

        )

        prompt = f"""
Context

{context}

Question

{question}

Answer using ONLY the context above.
"""

        response = self.generate(prompt)

        return {

            "context": context,

            "response": response,

        }

    def run(self, question: str):
        return self.ask(question)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]