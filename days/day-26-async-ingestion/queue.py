from shared_core.jobs import Queue 

class PgBossQueue(Queue):
    def __init__(self, boss):
        self.boss=boss 
    
    async def publish(self, topic,payload):
        return await self.boss.send(topic, payload)