from shared_core.database import SQLiteClient

class Database:
    def __init__(self):
        self.db=SQLiteClient("sample.db")

    def execute(self,sql:str):
        return self.db.execute(sql)
        