from .memory import ConversationMemory

class ConversationManager:

    def __init__(self):
        self.memory=ConversationMemory()

    def add_user_message(self, text:str):
        self.memory.history.add("user",text)

    def add_assistant_message(self, text:str):
        self.memory.history.add("assistant",text)

    def messages(self):
        return self.memory.history.messages

    def clear(self):
        self.memory.history.clear()

    