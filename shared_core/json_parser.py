import json 

class JSONParser:
    @staticmethod
    def parse(text:str):
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON returned by LLM.\n\n{text}"
            ) from exc
            