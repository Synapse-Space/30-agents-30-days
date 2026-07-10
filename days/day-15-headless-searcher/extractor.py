from playwright.sync_api import Page 

class PageExtractor:
    def extract(self,page:Page,url:str):
        page.goto(url,wait_until="domcontentloaded")

        page.locator("script").evaluate_all("(nodes)=>nodes.forEach(n=>n.remove())")
        page.locator("style").evaluate_all("(nodes)=>nodes.forEach(n=>n.remove())")

        title=page.title()
        body=page.locator("body").inner_text()

        return {
            "title":title,
            "body":body,
            "url":url
        }