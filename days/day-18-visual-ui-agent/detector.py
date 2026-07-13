from pathlib import Path 
import ollama

class OllamaVisionDetector:
    def __init__(self, model="llama3.2-vision"):
        self.model=model 
        

    def detect(self,image:Path,instruction:str,prompt:str):
        response=ollama.chat(
            model=self.model,
            messages=[{
                "role":"user",
                "content": prompt

                    + "\n"

                    + instruction,

                    "images": [

                        str(image)

                    ],
            }],
            format="json"
        )
        return response["message"]["content"]

