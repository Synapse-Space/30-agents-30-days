import psycopg 
from pgvector.psycopg import register_vector
from shared_core.knowledge import VectorRepository

class PgVectorRepository(VectorRepository):
    def __init__(self, connection):
        self.connection=psycopg.connect(connection)
        register_vector(self.connection)

    def save(self, chunk):
        with self.conncetion.cursor() as cursor:
            cursor.execute("""
            INSERT INTO document_chunks(document_id, chunk_index, content, embedding)
            VALUES (%s, %s, %s, %s)
            """, (chunk.document_id, chunk.index, chunk.text, chunk.embedding))

        self.connection.commit()
    