from playwright.sync_api import sync_playwright

class PlaywrightClient:
    def __init__(self, headless: bool=True):
        self.headless=headless
        self.playwright=None
        self.browser=None 

    def start(self):
        self.playwright=sync_playwright().start()
        self.browser=self.playwright.chromium.launch(headless=self.headless)
    
        return self.browser

    
    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
            