from shared_core.agents import StatefulAgent
from alert_engine import AlertEngine
from market_provider import MarketProvider

SYSTEM_PROMPT="""You are an FX Market Assistant. Explain market movements clearly. Be concise."""

class FXSentinelAgent(StatefulAgent):
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
        self.market=MarketProvider()
    
    def monitor(self, context,base,target,threshold,direction):
        rate=self.market.get_rate(base,target)
        previous=context.state.get(f"{base}_{target}")
        triggered=(AlertEngine.should_alert(rate,threshold,direction))

        context.state[f"{base}_{target}"]={
            "last_rate":rate,
            "threshold":threshold,
            "direction":direction
        }

        self.save_context(context)

        
        return {
            "current_rate":rate,
            "previous":previous,
            "alert":triggered
        }


    