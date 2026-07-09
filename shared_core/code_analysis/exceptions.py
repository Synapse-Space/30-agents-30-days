class CodeAnalysisException(Exception):
    pass

class FileNotPythonError(CodeAnalysisException):
    def __init__(self,file_path):
        super().__init__(f"The file {file_path} is not a python file")