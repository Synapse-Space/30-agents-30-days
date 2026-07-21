def build_summary(

    filename,

    chunks,

):

    return f"""
Knowledge ingestion finished.

Document:

{filename}

Chunks:

{chunks}

Summarize the ingestion process.
"""