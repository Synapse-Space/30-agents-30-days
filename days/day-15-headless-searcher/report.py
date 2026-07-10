def build_summary_prompt(documents):
    joined="\n\n".join(documents)
    return f""""Summarize the following research. {joined}"""

    