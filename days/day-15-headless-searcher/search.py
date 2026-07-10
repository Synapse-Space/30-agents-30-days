from playwright.sync_api import Page 

from shared_core.browser import SearchEngine, SearchResult

class GoogleSearcher:
    def __init__(self):
        self.engine=SearchEngine()

    def search(self,page:Page,query:str,limit=3)->list[SearchResult]:
        url=self.engine.build_url(query)
        page.goto(url,wait_until="networkidle")
        results=[]
        cards=page.locator("div.g").all()

        for card in cards:
            try:
                title=card.locator("h3").inner_text()
                href=card.locator("a").first_get_attribute("href")
                snippet=""

                try:
                    snippet=card.locator(".VwiC3b").inner_text()
                
                except Exception:
                    pass
                
                if href:
                    results.append(SearchResult(title=title,url=href,snippet=snippet))

                
                except Exception:
                    continue
                
                if len(results)>=limit:
                    break

        return results

    