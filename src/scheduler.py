class Scheduler:
    def __init__(self):
        self.scheduled_events = []

    def schedule_event(self, title, date, time):
        if not title or not date or not time:
            raise ValueError("Title, date, and time are required for scheduling an event")

        event = {
            'title': title,
            'date': date,
            'time': time
        }

        self.scheduled_events.append(event)

    def get_scheduled_events(self):
        return self.scheduled_events.copy()