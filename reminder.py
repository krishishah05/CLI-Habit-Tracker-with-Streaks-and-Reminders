# reminder.py
import datetime

def send_reminder(habit_manager):
    today = datetime.date.today().isoformat()
    reminders = []

    for habit, data in habit_manager.habits.items():
        if data['last_completed'] != today:
            reminders.append(habit)

    if reminders:
        print("\n** Reminder: You still need to complete these habits today! **")
        for habit in reminders:
            print(f"- {habit}")
