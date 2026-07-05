from .models import Memory

class MemoryRepository:

    def __init__(self,postgres):
        self.postgres=postgres

    
    def save(self,memory:Memory):
        with self,postgres.connection() as conn:
            withconn.cursor() as cur:
                cur.execute( """
                    INSERT INTO memories
                    (
                        id,
                        user_id,
                        key,
                        value,
                        created_at
                    )
                    VALUES
                    (%s,%s,%s,%s,%s)
                    """,(
                        memory.id,
                        memory.user_id,
                        memory.key,
                        memory.value,
                        memory.created_at
                    ))

    def find_by_user(self, user_id:str):
        with self.postgres.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT key,value FROM memories WHERE user_id=%s""",(user_id))

                return cur.fetchall()