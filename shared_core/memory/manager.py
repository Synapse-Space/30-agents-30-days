from .models import Memory

class MemoryManager:
    def __init__(self, repository):
        self.repository=(repository)

    
    
    def remembet(self, user_id, key, value):
        memory=Memory(
            user_id=user_id,
            key=key,
            value=value,
        )

        self.repository.save(memory)

    def recall(self, user_id):
        rows= self.repository.find_by_user(user_id)

        return { key:value 
        for key,value in rows}
