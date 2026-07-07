import re

class ParagraphSplitter:
    def split(self, text:str)->list[str]:
        parts=re.split(r"\n\s*\n",text.strip())

        return [p.strip() for p in parts if p.strip()]
        