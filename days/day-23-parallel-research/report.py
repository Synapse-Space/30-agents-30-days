class ExecutiveReportGenerator:
    def __init__(self, llm):
        self.llm=llm 

    def run(self, state):
        prompt=f""" Research Topic: {state.query}
        
        Market Report:
        {state.market}

        Technology Analysis:
        {state.technology}

        Trends:
        {state.trends}

        Create a Unified executive report.
        """

        state.executive_report=self.llm.invoke(prompt)
        return state 