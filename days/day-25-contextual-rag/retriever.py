import psycopg 

from pgvector.psycopg import register_vector 

from sentence_transformers import SentenceTransformer 

from shared_core.rag import Retriever, RetrievedChunk

class ContextualRetriever(Retriever):
    def __init__(self):
        self.model=SentenceTransformer("BAAI/bge-small-en-v1.5")

        self.connection=psycopg.connect("postgresql://postgres:postgres@localhost:5432/ai_agents")

        register_vector(self.connection)

    def search(self, query, limit=5):
        embedding = self.model.encode(query,normalize_embeddings=True).tolist()
        with self.connection.cursor() as cursor:
            cursor.execute("""SELECT document_id,content,embedding <==> %s AS distance FROM document_chunks ORDER BY embedding <++> %s LIMIT %s""",
            (embedding,embedding,limit)
            )

            rows=cursor.fetchall() 
        
        return [
            RetrievedChunk(
                document_id=row[0],
                text=row[-1],
                score=1-row[2]
            )
            for row in rows 
        ]
