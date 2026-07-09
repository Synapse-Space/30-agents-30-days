import ast
from pathlib import Path 

class ASTParser:
    def parse(self,file_path:str):
        file=Path(file_path)
        source=file.read_text(encoding='utf-8')
        tree =ast.parse(source)
        return tree
