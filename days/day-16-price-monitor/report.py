def build_summary_prompt(
    changes,
):

    lines = []

    for change in changes:

        lines.append(

            f"{change.title}: "

            f"{change.previous} -> "

            f"{change.current} "

            f"({change.percentage}%)"

        )

    joined = "\n".join(lines)

    return f"""
Price Changes

{joined}

Summarize the overall market movement.
"""