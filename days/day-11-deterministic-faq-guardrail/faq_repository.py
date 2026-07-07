import json

from models import FAQ

class FAQRepository:
    def __init__(self, path="sample_faq.json"):
        self.path = path


    def get_all(self):
        with open(self.path,"r",encoding="utf-8") as f:
            data=json.load(f)

        return [FAQ(**item) for item in data]       