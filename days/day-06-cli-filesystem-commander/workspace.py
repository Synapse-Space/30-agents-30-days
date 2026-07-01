from pathlib import Path 

class Workspace:
    def __init__(self, root: str="workspace"):
        self.root=Path(root).resolve()
        self.root.mkdir(
            parents=True,
            exist_ok=True
        )
    
    def resolve( self, relative_path:str)->Path:
        path=(self.root/relative_path).resolve()

        if self.root not in path.parents and path!=self.root:
            raise PermissionError(" Path is outside workspace.")

        return path