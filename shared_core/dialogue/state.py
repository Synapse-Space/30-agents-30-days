from pydantic import BaseModel, Field 

class ConversationState(BaseModel):
    session_id:str 
    current_engine:str="rasa"
    active_form:str|None=None 
    slots:dict=Field(default_factory=dict)
    history:list=Field(default_factory=list)
    context:dict=Field(default_factory=dict)