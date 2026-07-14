class RecoveryManager:
    def next_candidate(self,plan):
        if not plan["alternatives"]:
            return None 

        return plan["alternatives"][0]