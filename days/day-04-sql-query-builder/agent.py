from shared_core.agents import StructuredAgent
from shared_core.database import (SQLiteClient, SchemaLoader)
from schema import SQLQuery
from prompts import SYSTEM_PROMPT
from database import Database
from sql_validator import SQLValidator

class SQLAgent(StructuredAgent):
    @property
    def schema(self):
        return SQLQuery
    
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
        self.database=Database()
        sqlite=SQLiteClient("sample.db")
        self.schema_loader=SchemaLoader(sqlite)

    def run(self, question:str):
        self.clear_history()
        schema=self.schema_loader.as_prompt()
        self.add_user_message(
            f"""
            Database Schema
            {schema}
            User Question
            {question}
            """
        )
        
        generated=self.generate()
        SQLValidator.validate(generated.sql)
        rows = self.database.execute(generated.sql)
        return {
            "question": question,
            "sql": generated.sql,
            "explanation": generated.explanation,
            "rows": rows,
        }
