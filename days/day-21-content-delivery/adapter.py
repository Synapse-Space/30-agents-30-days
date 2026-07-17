class CMSAdapter:
    def open_editor(self,page):
        print("Opened editor")

    
    def fill_title(self, page, title):
        print(f"Filled title: {title}")
    
    def fill_body(self, page, body):
        print(f"Filled body: {len(body)} characters")
    
    def save_draft(self, page):
        print("Saved draft")
    