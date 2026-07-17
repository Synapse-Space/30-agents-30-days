def build_summary(result):

    return f"""
Publishing completed.

Status:

{result['status']}

Preview:

{result['preview_url']}

Explain the publishing result.
"""