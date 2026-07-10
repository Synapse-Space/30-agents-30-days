from urllib.parse import quote

class SearchEngine:
    BASE_URL="https://en.wikipedia.org/w/index.php?search="

    def build_url(self,query:str):
        return self.BASE_URL+quote(query)

    