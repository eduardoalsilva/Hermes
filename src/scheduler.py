import sqlite3
from datetime import datetime

class Scheduler:
    def __init__(self, db_path='scheduler.db'):
        self.scheduled_events = []
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events(
                    title TEXT,
                    date TEXT,
                    time TEXT
                )
                
            ''')

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
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events')
            rows = cursor.fetchall()
            self.scheduled_events = [{'title': row[0], 'date': row[1], 'time': row[2]} for row in rows]
        return self.scheduled_events.copy()

    def edit_event(self, old_title, new_title, new_date, new_time):
        for event in self.scheduled_events:
            if event['title'] == old_title:
                event['title'] = new_title
                event['date'] = new_date
                event['time'] = new_time

    def delete_event(self, title):
        self.scheduled_events = [event for event in self.scheduled_events if event['title'] != title]

    def set_reminder(self, title, minutes_before):
        if event['title'] == title:
            reminder_time = event['time'] - timedelta(minutes=minutes_before)

            print(f'Reminder: The event "{event['title']}" will occur in {minutes_before} minutes, at {reminder_time}.')

    def save_to_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM events')
            for event in self.schedule_events:
                cursor.execute('INSERT INTO events VALUES (?, ?, ?)', (event['title'], event['date'], event['time']))

    def load_from_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events')
            rows = cursor.fetchall()
            self.scheduled_events = [{'title': row[0], 'date': row[1], 'time': row[2]} for row in rows]
            