class ExecutiveReportGenerator:
    def __init__(self, llm):
        self.llm=llm 

    def run(self, state):
        prompt=f""" Research Topic: {state.get('query', '')}
        
        Market Report:
        {state.get('market', '')}

        Technology Analysis:
        {state.get('technology', '')}

        Trends:
        {state.get('trends', '')}

        Create a Unified executive report.
        """

        response=self.llm.invoke(prompt)
        return {"executive_report": response.content}