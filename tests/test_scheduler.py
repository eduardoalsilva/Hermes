import unittest
import os
from datetime import datetime
import sqlite3
from src.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_scheduler.db'
        self._create_empty_database()
        self.scheduler = Scheduler(db_path=self.db_path)

    def _create_empty_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS events (title TEXT, date TEXT, time TEXT)')

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
    
    def test_schedule_and_retrieve_event(self):
        # scheduler = Scheduler()
        print("Initial state: ", self.scheduler.get_scheduled_events())

        title = "Team meeting"
        date = "2024-03-05"
        time = "14:00"
        self.scheduler.schedule_event(title, date, time)
        print("After scheduling event: ", self.scheduler.get_scheduled_events())
        
        scheduled_events = self.scheduler.get_scheduled_events()

        self.assertEqual(len(scheduled_events), 1)
        self.assertEqual(scheduled_events[0]['title'], title)
        self.assertEqual(scheduled_events[0]['date'], date)
        self.assertEqual(scheduled_events[0]['time'], time)

        print("After aseerting equality: ", self.scheduler.get_scheduled_events())

    def test_edit_event(self):
        title = 'New Event'
        date = '2024-03-04'
        time = '14:30'
        self.scheduler.schedule_event(title, date, time)

        new_title = 'Edited Event'
        new_date = '2024-03-04'
        new_time = '14:30'
        self.scheduler.edit_event(title, new_title, date, time)

        scheduled_events = self.scheduler.get_scheduled_events()
        self.assertEqual(len(scheduled_events), 1)
        self.assertEqual(scheduled_events[0]['title'], new_title)
        self.assertEqual(scheduled_events[0]['date'], new_date)
        self.assertEqual(scheduled_events[0]['time'], new_time)

    def test_delete_event(self):
        title = 'Event to Delete'
        date = '2024-03-04'
        time = '14:00'
        self.scheduler.schedule_event(title, date, time)

        self.scheduler.delete_event(title)
        scheduled_events = self.scheduler.get_scheduled_events()
        self.assertEqual(len(scheduled_events), 0)

    def test_set_reminder(self):
        title = 'Reminder Event'
        date = '2024-03-05'
        time = '08:00'
        self.scheduler.schedule_event(title, date, time)

        minutes_before = 15
        self.scheduler.set_reminder(title, minutes_before)

        scheduled_events = self.scheduler.get_scheduled_events()
        self.assertEqual(len(scheduled_events), 1)
        self.assertTrue('reminder' in scheduled_events[0])

if __name__ == '__main__':
    unittest.main()


# python -m unittest dicover /path/to/tests