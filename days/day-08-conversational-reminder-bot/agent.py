from shared_core.agents import (ConversationAgent)
from models import (Reminder, ReminderExtraction)

from prompts import SYSTEM_PROMPT
from scheduler import ReminderScheduler

class ReminderAgent(ConversationAgent):
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)

        self.scheduler=(ReminderScheduler())

    
    def run(self, user_message: str):
        return self.process(user_message)

    def process(self,user_message:str):
        self.user(user_message)

        extraction=self.generate_structured_output(user_message, ReminderExtraction)

        if extraction.needs_followup:
            self.assistant(
                extraction.followup_question
            )
            return {
                "type":"followup",
                "message":extraction.followup_question
            }
        reminder=Reminder(title=extraction.title,reminder_time=extraction.reminder_time)
        self.scheduler.schedule(reminder)
        response=(
            f"✅ Reminder created for "

            f"{reminder.reminder_time}"
        )

        self.assistant(response)

        return {
            "type":"success",
            "message":response
        }

