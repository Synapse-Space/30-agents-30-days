from pathlib import Path 
from .parser import ASTParser
from .visitor import CodeVisitor
from .models import ModuleInfo

class CodeAnalyzer:
    def __init__(self):
        self.parser=ASTParser()

    def analyze(self,file_path:str):
        tree=self.parser.parse(file_path)

        visitor=CodeVisitor()
        visitor.visit(tree)

        return ModuleInfo(

            path=str(
                Path(file_path)
            ),

            imports=visitor.imports,

            functions=visitor.functions,

            classes=visitor.classes,
        )