from .models import Chunk

class Chunker:
    def chunk(self, document, paragraphs)->list[Chunk]:
        chunks=[]
        for index, paragraph in enumerate(paragraphs):
            chunks.append(
                Chunk(
                    document_id=document.id,
                    chunk_number=index,
                    text=paragraph
                )
            )
        
        return chunks