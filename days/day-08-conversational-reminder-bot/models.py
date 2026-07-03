from datetime import datetime 
from typing import Optional
from pydantic import BaseModel

class Reminder(BaseModel):
    title:str 
    reminder_time:datetime 
    completed:bool=False

class ReminderExtraction(BaseModel):
    title:str
    reminder_time:Optional[datetime]=None
    needs_followup:bool=False
    followup_question:Optional[str]=None
    
