from playwright.sync_api import Browser 

from .storage import StorageStateManager

class AuthenticationManager:
    def __init__(self,storage_path:str="storage_state.json"):
        self.storage=StorageStateManager(storage_path)

    def new_context(self,browser:Browser):
        if self.storage.exists():
            return browser.new_context(storage_state=self.storage.get_path())
        
        return browser.new_context()

    def save_context(self,context):
        context.storage_state(path=self.storage.get_path())

        
    