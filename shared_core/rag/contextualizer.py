class Contextualizer:

    def build(

        self,

        summary,

        chunk,

    ):

        return f"""

Document Summary

{summary}

----------------

Chunk

{chunk.text}

"""