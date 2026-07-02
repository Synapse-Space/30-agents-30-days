import uuid
from .context import AgentContext
from .state_store import JSONStateStore

class ContextManager:
    def __init__(self):
        self.store=JSONStateStore()

    def load_context(self, session_id:str | None=None)-> AgentContext:
        if session_id is None:
            session_id=str(uuid.uuid4())

        state=self.store.load()
        return AgentContext(session_id=session_id,state=state.get(session_id,{}))


    def save_context(self,context:AgentContext):
        state=self.store.load()
        state[context.session_id]=context.state

        self.store.save(state)
        