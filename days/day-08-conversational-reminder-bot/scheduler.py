from models import Reminder
from reminder_store import (ReminderStore)

class ReminderScheduler:
    def __init__(self):
        self.store=ReminderStore()
    
    def schedule(self, reminder:Reminder):
        self.store.add(reminder)