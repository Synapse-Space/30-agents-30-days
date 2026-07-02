class AlertEngine:
    @staticmethod
    def should_alert(rate:float,threshold:float,direction:str):
        if direction=="above":
            return rate>=threshold
        return rate<=threshold