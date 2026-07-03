from datetime import datetime
import time 

from reminder_store import (ReminderStore)

class ReminderWorker:
    def __init__(self):

        self.store=ReminderStore()
    
    def start(self):
        print("Reminder worker started...")

        while True:
            reminders=self.store.load()
            changed=False
            now=datetime.now()
            for reminder in reminders:
                reminder_time_naive = reminder.reminder_time.replace(tzinfo=None)
                if(not reminder.completed and reminder_time_naive<=now):
                    print()
                    print("="*50)
                    print(
                        "🔔 REMINDER"
                    )

                    print(
                        reminder.title
                    )

                    print("=" * 50)

                    print()

                    reminder.completed = True

                    changed = True
                
            if changed:
                self.store.save(reminders)

            time.sleep(5)
            