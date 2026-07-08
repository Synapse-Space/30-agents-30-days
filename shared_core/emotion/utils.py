import re

def tokenizer(text: str)->list[str]:

    return re.findall(r"[a-zA-Z0-9']+", text.lower())