# from .models import Chunk

# class Chunker:
#     def chunk(self, document, paragraphs)->list[Chunk]:
#         chunks=[]
#         for index, paragraph in enumerate(paragraphs):
#             chunks.append(
#                 Chunk(
#                     document_id=document.id,
#                     chunk_number=index,
#                     text=paragraph
#                 )
#             )
        
#         return chunks

from .models import Chunk 

class TextChunker:
    def chunk(self,document,size=500):
        chunks=[]
        text=document.content 
        for i in range(0,len(text),size):
            chunks.append(
                Chunk(
                    document_id=document.id,
                    index=len(chunks),
                    text=text[i:i+size]
                )
            )
        return chunks