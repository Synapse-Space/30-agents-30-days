from pathlib import Path 
from .models import Document 

class DocumentLoader:
    def load(self, filepath):
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        if path.suffix.lower() == ".pdf":
            try:
                import pypdf
                reader = pypdf.PdfReader(str(path))
                text = "\n\n".join(page.extract_text() or "" for page in reader.pages)
            except Exception as e:
                text = path.read_text(encoding="utf-8", errors="ignore")
        else:
            text = path.read_text(encoding="utf-8", errors="ignore")
            
        return Document(id=path.stem, source=str(filepath), content=text)