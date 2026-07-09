from pathlib import Path 

def is_python_file(file_path:str)->bool:
    return Path(file_path).suffix=='.py'