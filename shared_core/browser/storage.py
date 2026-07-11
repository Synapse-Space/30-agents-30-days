from pathlib import Path 

class StorageStateManager:
    def __init__(self,path: str="storage_state.json"):
        self.path=Path(path)

    def exists(self):
        return self.path.exists()

    def get_path(self):
        return str(self.path)
        