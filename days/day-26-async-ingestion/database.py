import psycopg 
from pgvector.psycopg import register_vector
from shared_core.knowledge import VectorRepository

class PgVectorRepository(VectorRepository):
    def __init__(self, connection_string):
        self.connection = psycopg.connect(connection_string)
        register_vector(self.connection)
        
        with self.connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id SERIAL PRIMARY KEY,
                    document_id VARCHAR(255),
                    chunk_index INTEGER,
                    content TEXT,
                    embedding VECTOR(384)
                );
            """)
        self.connection.commit()

    def save(self, chunk):
        with self.connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO document_chunks(document_id, chunk_index, content, embedding)
            VALUES (%s, %s, %s, %s::vector)
            """, (chunk.document_id, chunk.index, chunk.text, chunk.embedding))

        self.connection.commit()
