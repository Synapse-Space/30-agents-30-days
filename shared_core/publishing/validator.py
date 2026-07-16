class ContentValidator:
    def validate(self,draft):
        if not draft.title:
            raise ValueError("Missing title.")
        
        if not draft.body:
            raise ValueError("Empty content.")

        
        return True