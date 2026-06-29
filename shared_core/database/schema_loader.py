from shared_core.database.sqlite_client import (SQLiteClient)

class SchemaLoader:
    def __init__(self, db:SQLiteClient):
        self.db=db

    def load(self):
        tables=self.db.execute(
            """
            SELECT name FROM sqlite_master WHERE type='table';            
            """
        )
        schema=[]

        for table in tables:
            table_name=table["name"]
            columns=self.db.execute(
                f"PRAGMA table_info({table_name})"
            )

            schema.append({
                "table":table_name,
                "columns":columns,
            })

        return schema

    def as_prompt(self):
        schema=self.load()
        prompt=""

        for table in schema:
            prompt +=( f"Table: {table['table']}\n")

            for column in table['columns']:
                prompt += (
                    f"-{column['name']}"
                    f"({column['type']})\n"
                )
            prompt += "\n"
        return prompt