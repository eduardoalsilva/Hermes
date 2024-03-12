from datetime import datetime, timedelta
from scheduler import Scheduler
import time

class ReminderService:
    @staticmethod
    def schedule_reminder(event_time, reminder_minutes):

        reminder_time = event_time - timedelta(minutes=reminder_minutes)
        return reminder_time
    
    @staticmethod
    def send_reminder(reminder_info):
        print(f"Send reminder to '{reminder_info['title']} at {reminder_info['reminder_time']}")

    @staticmethod
    def process_reminders(scheduler):
        while True:
            scheduled_events = Scheduler.get_scheduled_events()

            for event in scheduled_events:
                if 'reminder' in event:
                    if datetime.now() >= event['reminder_time']:
                        print(f"Reminder to '{event['title']}' sent!")

                        scheduler.remove_reminder(event['title'])

                    else:
                        print(f"Reminder to '{event['title']} scheduled to {event['reminder_time']}")
                
            time.sleep(60)