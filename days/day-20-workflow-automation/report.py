def build_summary(result):

    return f"""
Workflow completed.

Status:

{result.status}

Completed Steps:

{result.completed_steps}

Explain the execution outcome.
"""