from playwright.sync_api import Page 

from shared_core.browser import SearchEngine, SearchResult

class GoogleSearcher:
    def __init__(self):
        self.engine=SearchEngine()

    def search(self,page:Page,query:str,limit=3)->list[SearchResult]:
        url=self.engine.build_url(query)
        page.goto(url,wait_until="networkidle")
        results=[]
        cards=page.locator("li.mw-search-result").all()

        for card in cards:
            try:
                title=card.locator(".mw-search-result-heading a").first.inner_text()
                href="https://en.wikipedia.org" + card.locator(".mw-search-result-heading a").first.get_attribute("href")
                snippet=""

                try:
                    snippet=card.locator(".searchresult").first.inner_text()
                
                except Exception:
                    pass
                
                if href:
                    results.append(SearchResult(title=title,url=href,snippet=snippet))

            except Exception:
                continue

            if len(results)>=limit:
                break

        return results

    