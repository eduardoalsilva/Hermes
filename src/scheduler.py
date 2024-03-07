import sqlite3
from datetime import timedelta, datetime

class Scheduler:
    def __init__(self, db_path='scheduler.db'):
        self.scheduled_events = []
        self.db_path = db_path
        self._create_table()

    def _create_table(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DROP TABLE IF EXISTS events')

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events(
                    title TEXT,
                    date TEXT,
                    time TEXT,
                    reminder TEXT
                )
                
            ''')

    def schedule_event(self, title, date, time):
        if not title or not date or not time:
            raise ValueError("Title, date, and time are required for scheduling an event")

        print(f"Scheduling event: {title}, {date}, {time}")

        with sqlite3.connect(self.db_path) as conn:
            conn.execute('INSERT INTO events (title, date, time) VALUES (?, ?, ?)', (title, date, time))

    def get_scheduled_events(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT title, date, time, reminder FROM events')
            events = [{'title': row[0], 'date': row[1], 'time': row[2], 'reminder': row[3]} for row in cursor.fetchall()]
            return events

    def edit_event(self, old_title, new_title, new_date, new_time):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
            UPDATE events
            SET title=?, date=?, time=?
            WHERE title=?    
        ''',(new_title, new_date, new_time, old_title))

    def delete_event(self, title):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM events WHERE title=?', (title,))

    def get_event_time(self, title):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT date, time FROM events WHERE title=?', (title,))
            result = cursor.fetchone()
            if result:
                date, time = result
                event_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                return event_time
            return None

    def set_reminder(self, title, minutes_before):
        event = next((e for e in self.scheduled_events if e['title'] == title), None)

        if event:
            event_time = datetime.strptime(event['time'], '%H:%M')

            reminder_time = event_time - timedelta(minutes=minutes_before)

            with sqlite3.connect(self.db_path) as conn:
                conn.execute('UPDATE events SET reminder=? WHERE title=?', (reminder_time.strftime('%H:%M'), title))            

            print(f'Reminder: The event "{title}" will occur in {minutes_before} minutes')

        else:
            print(f'Event "{title}" not found.')

        for event in self.scheduled_events:
            if event['title'] == title:
                reminder_time = event['time'] - timedelta(minutes=minutes_before)

                print(f'Reminder: The event "{event['title']}" will occur in {minutes_before} minutes, at {reminder_time}.')

    def save_to_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM events')
            for event in self.schedule_event:
                cursor.execute('INSERT INTO events VALUES (?, ?, ?)', (event['title'], event['date'], event['time']))

    def load_from_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events')
            rows = cursor.fetchall()
            self.scheduled_events = [{'title': row[0], 'date': row[1], 'time': row[2]} for row in rows]
            