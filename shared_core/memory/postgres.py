import psycopg

class PostgresClient:
    def __init__(self, connection_string:str):
        self.connection_string=(
            connection_string
        )
    
    def connection(self):
        return psycopg.connect(
            self.connection_string
        )
        