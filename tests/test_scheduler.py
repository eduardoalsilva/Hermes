import unittest
from datetime import datetime
from src.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def test_schedule_event(self):
        scheduler = Scheduler()

        title = "Reunião de Equipe"
        date = "2024-03-01"
        time = "14:00"

        scheduler.schedule_event(title, date, time)

        scheduled_events = scheduler.get_scheduled_events()

        self.assertEqual(len(scheduled_events), 1)
        self.assertEqual(scheduled_events[0]['title'], title)
        self.assertEqual(scheduled_events[0]['date'], date)
        self.assertEqual(scheduled_events[0]['time'], time)

    def test_get_scheduled_events(self):
        scheduler = Scheduler()

        events_data = [
            {"title": "Reunião de Equipe", "date": "2024-03-01", "time": "14:00"},
            {"title": "Apresentação do Projeto", "date": "2024-03-02", "time": "10:30"},
            {"title": "Almoço de Equipe", "date": "2024-03-03", "time": "12:00"},
            {"title": "", "date": "2024-03-02", "time": "10:30"},
            {"title": "Almoço de Equipe", "date": "", "time": "12:00"},
            {"title": "Almoço de Equipe", "date": "2024-03-03", "time": " "}
        ]

        for event_data in events_data:
            scheduler.schedule_event(event_data['title'], event_data['date'], event_data['time'])

        scheduled_events = scheduler.get_scheduled_events()

        self.assertEqual(len(scheduled_events), len(events_data))

        for i in range(len(events_data)):
            self.assertEqual(scheduled_events[i]['title'], events_data[i]['title'])
            self.assertEqual(scheduled_events[i]['date'], events_data[i]['date'])
            self.assertEqual(scheduled_events[i]['time'], events_data[i]['time'])


if __name__ == '__main__':
    unittest.main()