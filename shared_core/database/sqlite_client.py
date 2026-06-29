import sqlite3

class SQLiteClient:
    def __init__(self, database:str):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory=(
            sqlite3.Row
        )
    
    def execute(self, query:str, parameters=None):
        cursor=self.connection.cursor()
        cursor.execute(query, parameters or [])
        return [dict(row) for row in cursor.fetchall()]

    def close(self):
        self.connection.close()
        