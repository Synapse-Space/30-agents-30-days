from playwright.sync_api import Page 

class HydrationManager:
    def wait_for_content(self, page:Page, selector:str, timeout:int=10000):
        page.wait_for_selector(selector,timeout=timeout)

        