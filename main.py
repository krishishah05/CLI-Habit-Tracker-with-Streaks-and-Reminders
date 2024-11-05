# main.py
from habit_manager import HabitManager
from reminder import send_reminder
import time

def display_menu():
    print("\nWelcome to the CLI Habit Tracker!")
    print("1. Add a new habit")
    print("2. Mark habit as complete")
    print("3. View habits and streaks")
    print("4. Exit")

def main():
    manager = HabitManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            habit_name = input("Enter the name of the habit: ").strip()
            manager.add_habit(habit_name)
            print(f"Habit '{habit_name}' added.")
        
        elif choice == '2':
            habit_name = input("Enter the name of the habit to mark as complete: ").strip()
            if manager.mark_habit_complete(habit_name):
                print(f"Habit '{habit_name}' marked as complete.")
            else:
                print(f"Habit '{habit_name}' not found.")
        
        elif choice == '3':
            manager.view_habits()
        
        elif choice == '4':
            print("Thank you for using the CLI Habit Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)  # Simulate delay for user experience
        send_reminder(manager)  # Daily reminder to keep streaks alive

if __name__ == "__main__":
    main()
