class CMSAdapter:
    def open_editor(self,page):
        raise NotImplementedError

    
    def fill_title(self, page, title):
        raise NotImplementedError
    
    def fill_body(self, page, body):
        raise NotImplementedError
    
    def save_draft(self, page):
        raise NotImplementedError
    