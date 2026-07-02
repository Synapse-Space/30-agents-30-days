import json
from pathlib import Path 
from typing import Any

class JSONStateStore:
    def __init__(self,path:str="storage/state.json"):
        self.path=Path(path)

        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.save({})

    def load(self)->dict[str,Any]:
        with open(self.path,"r",encoding="utf-8") as file:
            return json.load(file)

    def save(self,data: dict[str,Any]):
        with open(self.path,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4)