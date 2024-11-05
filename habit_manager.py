# habit_manager.py
import json
import datetime
from file_operations import save_habits, load_habits

class HabitManager:
    def __init__(self):
        self.habits = load_habits()

    def add_habit(self, habit_name):
        self.habits[habit_name] = {
            'streak': 0,
            'last_completed': None
        }
        save_habits(self.habits)

    def mark_habit_complete(self, habit_name):
        if habit_name in self.habits:
            today = datetime.date.today().isoformat()
            last_completed = self.habits[habit_name]['last_completed']

            if last_completed == today:
                print("Habit already completed today!")
                return False

            if last_completed == (datetime.date.today() - datetime.timedelta(days=1)).isoformat():
                self.habits[habit_name]['streak'] += 1
            else:
                self.habits[habit_name]['streak'] = 1

            self.habits[habit_name]['last_completed'] = today
            save_habits(self.habits)
            return True
        return False

    def view_habits(self):
        if not self.habits:
            print("No habits to display.")
            return

        print("\nCurrent Habits and Streaks:")
        for habit, data in self.habits.items():
            streak = data['streak']
            last_completed = data['last_completed']
            print(f"- {habit} | Streak: {streak} days | Last completed: {last_completed or 'Never'}")
