# Simple To-Do List App (Console Version)

FILENAME = "tasks.txt"

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found yet.")

def add_task():
    task = input("Enter new task: ")
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(f"✅ '{task}' added successfully.")

def delete_task():
    view_tasks()
    try:
        num = int(input("\nEnter task number to delete: "))
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Removed: {removed.strip()}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
