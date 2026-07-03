import json
from pathlib import Path 
from models import Reminder

class ReminderStore:
    def __init__(self):
        self.path=Path("storage/reminders.json")

        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text("[]")

    def load(self):
        data=json.loads(self.path.read_text())
        return [Reminder.model_validate(item) for item in data]

    def save(self,reminders):
        self.path.write_text(
            json.dumps([
                r.model_dump(mode="json")
                for r in reminders
            ],
            indent=4
            )
        )
    
    def add(self, reminder:Reminder):
        reminders=self.load()
        reminders.append(reminder)
        self.save(reminders)
        