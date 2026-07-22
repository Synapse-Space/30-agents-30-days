def build_summary(

    question,

    chunks,

):

    return f"""
Question:

{question}

Retrieved Chunks:

{len(chunks)}

Explain why these chunks were
selected.
"""