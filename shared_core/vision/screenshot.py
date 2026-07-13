from pathlib import Path 
from playwright.sync_api import Page 

class ScreenshotManager:
    def capture(self, page:Page,path="page.png",full_page=True):
        page.screenshot(path=path, full_page=full_page)

        return Path(path)
        