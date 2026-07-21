# from pathlib import Path 
# from .models import Document

# class DocumentLoader:
#     SUPPORTED_TYPES={".txt",".md"}

#     def load(self, path:str)->Document:
#         file=Path(path)
#         if not file.exists():
#             raise FileNotFoundError(path)
        
#         if file.suffix not in self.SUPPORTED_TYPES:
#             raise ValueError(f"unsupported_format{file.suffix}")

    
#         return Document(
#             name=file.name,
#             path=str(file),
#             content=file.read_text(encoding="utf-8"),
            
#         )

#     def load_directory(self, directory:str)->list[Document]:
#         docs=[]
#         folder=Path(directory)
#         for file in folder.iterdir():
#             if file.suffix in self.SUPPORTED_TYPES:
#                 docs.append(self.load(str(file)))
#         return docs

from pathlib import Path 
from .nodels import Document 

class DocumentLoader:
    def load(self, filepath):
        text=Path(filepath).read_text()
        return Document(id=Path(filepath).stem,source=filepath,content=text)
        