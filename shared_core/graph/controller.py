class ReflectionController:
    def __init__(self, threshold=0.85):
        self.threshold = threshold 

    
    def next(self, state):
        if state.get("score", 0.0) >= self.threshold:
            return "finish"
        
        if state.get("iteration", 0) >= state.get("max_iterations", 5):
            return "finish"

        
        return "writer"
        
        