from dateutil import parser

class NLPParser:
    @staticmethod
    def parse_command(command):

        parsed_info = {
            'title': 'Default event',
            'date': '2024-03-08',
            'time': '12:00',
            'reminder_minutes': 15,
        }

        try:
            parsed_date_time = parser.parse(command, fuzzy=True)
            parsed_info['date'] = parsed_date_time.strftime('%Y-%m-%d')
            parsed_info['time'] = parsed_date_time.strftime('%H:%M')
        except ValueError:
            print("Failed to extract date and time information.")

        return parsed_info