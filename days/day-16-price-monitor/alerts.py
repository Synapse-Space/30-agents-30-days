from models import PriceStatus

class AlertEngine:
    def generate(self,changes):
        alerts=[]

        for change in changes:
            if change.status==PriceStatus.DECRESED:
                alerts.append(
                    f"Product {change.title} price dropped by {change.percentage}% ({change.current})"
                )
            elif change.status==PriceStatus.INCRESED:
                alerts.append(
                    f"Product {change.title} price increased by {change.percentage}% ({change.current})"
                )
        
        return alerts