from review_models import (ReviewFinding, Severity)

class RulesEngine:
    def evaluate(self,module):
        findings=[]
        for function in module.functions:
            if not function.has_docstring:
                findings.append(
                    ReviewFinding(
                        rule="DOC001",
                        severity=Severity.WARNING,
                        line=function.line,
                        message=f"Function '{function.name}' is missing a docstring."

                    )
                )
            if not function.has_return_annotation:
                findings.append(
                    ReviewFinding(
                        rule="TYPE001",
                        severity=Severity.INFO,
                        line=function.line,
                        message=f"Function '{function.name}' has no return type annotation."
                    )
                )
            
            if len(function.arguments)>5:
                findings.append(
                    ReviewFinding(
                        rule="FUNC001",
                        severity=Severity.WARNING,
                        line=function.line,
                        message=f"Function '{function.name}' has more than 5 arguments."
                    )
                )
        
        for cls in module.classes:
            if not cls.has_docstring:
                findings.append(
                    ReviewFinding(
                        rule="DOC002",
                        severity=Severity.WARNING,
                        line=cls.line,
                        message=f"Class '{cls.name}' is missing a docstring."
                    )
                )
        
        score=max(100-len(findings)*5,0)

        return ReviewReport(
            findings=findings,
            score=score
        )