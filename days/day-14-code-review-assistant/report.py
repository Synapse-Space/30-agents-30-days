from review_models import ReviewReport

def build_review_prompt(report:ReviewReport):
    findings="\n".join(f"- {item.rule}: {item.message}" for item in report.findings)

    return f"""
Review Findings

{findings}

Overall Score

{report.score}/100

Explain these findings and recommend improvements.
"""