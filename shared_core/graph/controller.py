class ReflectionController:
    def __init__(self, threshold=0.85):
        self.threshold = threshold 

    
    def next(self, state):
        if state.score>=self.threshold:
            return "finish"
        
        if state.iteration>=state.max_iterations:
            return "finish"

        
        return "writer"
        
        