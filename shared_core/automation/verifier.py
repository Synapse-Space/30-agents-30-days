from playwright.sync_api import Page 

class ActionVerifier:
    def page_changed(self,page:Page,previous_url:str):
        return page.url!=previous_url

    def title_changed(self,page:Page,previous_title:str):
        return page.title()!=previous_title

        
