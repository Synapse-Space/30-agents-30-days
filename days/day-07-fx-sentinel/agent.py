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

    def run(self, alert_data: dict) -> str:
        self.clear_history()
        
        base = alert_data.get("base")
        target = alert_data.get("target")
        rate = alert_data.get("current_rate")
        
        prompt = f"The currency pair {base}/{target} just hit a rate of {rate}. Please provide a brief 1-2 sentence explanation of what this might mean for the market."
        self.add_user_message(prompt)
        
        response = self.chat()
        return response.get("message", {}).get("content", "No explanation generated.")


    