from shared_core.agents import (
    BrowserAgent,
)

from prompts import SYSTEM_PROMPT

from search import GoogleSearcher

from extractor import PageExtractor

from markdown import MarkdownBuilder

from report import build_summary_prompt


class HeadlessSearchAgent(BrowserAgent):
    def __init__(self,memory_manager):
        super().__init__(SYSTEM_PROMPT,memory_manager)
        self.searcher=GoogleSearcher()
        self.extractor=PageExtractor()
        self.markdown=MarkdownBuilder()


    def research(self,query:str):
        documents=[]

        with self.open_browser() as page:
            results=self.searcher.search(page, query)
            for result in results:
                page_data = self.extractor.extract(page, result.url)
                documents.append(
                    self.markdown.build(page_data)
                )
        
        prompt=build_summary_prompt(documents)

        summary=self.generate(prompt)

        return {
            "documents":documents,
            "summary":summary
        }

    def run(self, query: str):
        return self.research(query)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

