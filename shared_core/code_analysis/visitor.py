import ast
from .models import (FunctionInfo, ClassInfo)

class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions=[]
        self.classes=[]
        self.imports=[]

    def visit_Import(self,node):
        for alias in node.names:
            self.imports.append(alias.name)

        self.generic_visit(node)
    
    def visit_ImportFrom(self,node):
        module=node.module or ""
        self.imports.append(module)
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        info=FunctionInfo(name=node.name, line=node.lineno, arguments=[arg.arg for arg in node.args.args], has_docstring=(ast.get_docstring(node) is not None), has_return_annotation=(node.returns is not None), decorators=[ast.unparse(d) for d in node.decorator_list]
        )
        self.functions.append(info)
        self.generic_visit(node)
    

    def visit_ClassDef(self,node):
        methods=[]
        for child in node.body:
            if isinstance(child,ast.FunctionDef):
                methods.append(child.name)

        info=ClassInfo(name=node.name,line=node.lineno,methods=methods,has_docstring=(ast.get_docstring(node) is not None))
        self.classes.append(info)

        self.generic_visit(node)