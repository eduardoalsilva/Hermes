from nlp_parser import NLPParser
from reminder_service import ReminderService
from scheduler import Scheduler

def main():
    scheduler = Scheduler()
    reminder_service = ReminderService()

    import threading
    reminders_thread = threading.Thread(target=ReminderService.process_reminders, args=(scheduler,),daemon=True)
    reminders_thread.start()

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() == 'exit':
            break

        parsed_info = NLPParser.parse_command(user_input)

        scheduler.schedule_event(
            parsed_info['title'],
            parsed_info['date'],
            parsed_info['time']
        )

        event_time = scheduler.get_event_time(parsed_info['title'])

        reminder_time = ReminderService.schedule_reminder(event_time, parsed_info['reminder_minutes'])
        scheduler.set_reminder(parsed_info['title'], reminder_time)

        print(f"Event '{parsed_info['title']}' scheduled to {parsed_info['date']} at {parsed_info['time']} with reminder {parsed_info['reminder_minutes']} minutes before.")

    reminders_thread.join()
        # print("\nHermes Assistant - Event Scheduler")
        # print("1. Schedule Event")
        # print("2. View Scheduled Events")
        # print("3. Edit Event")
        # print("4. Delete Event")
        # print("5. Set Reminder")
        # print("6. Save and Quit")

        # try:
        #     choice = int(input("Enter your choice: (between 1 and 6)"))

        # except:
        #     print("Enter a integer! ")
        #     continue

        # if choice == 1:
        #     title = input("Enter event title: ")
        #     date = input("Enter event date (YYYY-MM-DD): ")
        #     time = input("Enter event time (HH:MM): ")
        #     scheduler.schedule_event(title, date, time)

        # elif choice == 2:
        #     events = scheduler.get_scheduled_events()
        #     if events:
        #         print("\nScheduled Events:")
        #         for event in events:
        #             print(f"{event['title']} on {event['date']} at {event['time']}")
                
        #     else:
        #         print("No events scheduled.")

        # elif choice == 3:
        #     title = input("Enter the title of the event to edit: ")
        #     new_title = input("Enter the new title: ")
        #     new_date = input("Enter the new date (YYYY-MM-DD): ")
        #     new_time = input("Enter the new time (HH:MM): ")
        #     # print("What data do you want to edit?")
        #     # print("1. Title")
        #     # print("2. Date")
        #     # print("3. Time")
        #     # while True:
        #     #     try:
        #     #         data_to_edit = int(input("Enter your choice between 1 and 3"))
        #     #         break
        #     #     except:
        #     #         print("Please enter a integer between 1 and 3")
        #     #         continue

        #     # if data_to_edit == 1:
        #     #     new_title = input("Enter the new title: ")
            
        #     # elif data_to_edit == 2:
        #     #     new_date = input("Enter the new date(YYYY-MM-DD): ")

        #     # elif data_to_edit == 3:
        #     #     new_time = input("Enter the new time (HH:MM):")

        #     scheduler.edit_event(title, new_title, new_date, new_time)

        # elif choice == 4:
        #     title = input("Enter the title of the event to delete: ")
        #     scheduler.delete_event(title)

        # elif choice == 5:
        #     title = input("Enter the title of the event for a reminder: ")
        #     minutes_before = int(input("Enter the number of minutes before the event for the reminder: "))
        #     scheduler.set_reminder(title, minutes_before)

        # elif choice == 6:
        #     scheduler.save_to_db()
        #     print("Events saved. Exiting")
        #     break

        # else:
        #     print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()