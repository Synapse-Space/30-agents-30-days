from urllib.parse import quote

class SearchEngine:
    BASE_URL="https://www.google.com/search?q="

    def build_url(self,query:str):
        return self.BASE_URL+quote(query)

    