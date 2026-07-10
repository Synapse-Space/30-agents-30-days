from .playwright_client import PlaywrightClient 

class BrowserSession:
    def __init__(self, headless=True):
        self.client=PlaywrightClient(headless)
        self.browser=None
        self.page=None

    def __enter__(self):
        self.browser=self.client.start()
        self.page=self.browser.new_page()
        return self.page

    def __exit__(self,exc_type,exc,tb):
        self.client.stop()
