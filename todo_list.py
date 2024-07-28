import os, json
from colorama import Fore, Style, Back, just_fix_windows_console

just_fix_windows_console()

# Project Constants
FILE_NAME = "tasks.json"
FILE_PATH = os.path.join(f"data/{FILE_NAME}")
PRIORITIES = ("high", "medium", "low")

# Create 'data' folder if not exists.
if not os.path.exists("data"):
    os.makedirs("data")

# Load the tasks from json file if it exists,
# if not, return empty list.
def load_tasks() -> list:
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as file:
                tasks = json.load(file)
                return tasks
        except json.JSONDecodeError:
            print(Fore.RED + "ُError loading file...")
            return []
    else:
        tasks = []
    return tasks

# Save tasks after modifying.
def save_tasks(tasks: list):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

# View the current tasks if it exists,
# if not return error message.
def view_tasks(tasks: list):
    if not tasks:
        print(Fore.RED + "\nNo tasks to view.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task.get("completed", False) else "❌"
            if task["priority"] == "high": task_color = Fore.LIGHTBLUE_EX
            elif task["priority"] == "medium": task_color = Fore.BLUE
            elif task["priority"] == "low": task_color = Fore.LIGHTCYAN_EX
            print(task_color + f"{i}. {task["task"]} (Priority: {task["priority"]}) - {status}")

def search_tasks(tasks: list):
    if not tasks:
        print(Fore.RED + "No tasks to view.")
        return
    
    while True:
        keyword = input(Fore.LIGHTWHITE_EX + "Enter keyword to search it: ").strip().lower()
        if keyword:
            break
        print(Fore.RED + "\nEnter valid keyword to search.\n")

    results = list(filter(lambda task: keyword in task["task"].lower(), tasks))
    print("\n")
    view_tasks(results)

# Add new task to the json file then save it. 
def add_task(tasks: list):
    task = input(Fore.LIGHTWHITE_EX + "Enter the task you want to add: ")
    while True:
        priority = input(Fore.LIGHTWHITE_EX + "Enter the task's priority (high, medium, low): ").strip().lower()
        if priority in PRIORITIES:
            break
        print(Fore.RED + "\nInvalid priority.\n")
    tasks.append({"task": task, "priority": priority, "completed": False})
    save_tasks(tasks)
    print(Fore.GREEN + f"\nTask '{task}' added with priority '{priority}'.")

# Edit existing task then save it.
def edit_task(tasks):
    if not tasks:
        print(Fore.RED + "No tasks to edit.")
        return
    view_tasks(tasks)
    
    try:
        task_index = int(input(Fore.LIGHTWHITE_EX + "\nEnter task's number to edit: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]    
            new_task = input(Fore.LIGHTWHITE_EX + "\nEnter new task: ").strip()
            if not new_task:
                new_task = task["task1"]
            while True:
                new_priority = input(Fore.LIGHTWHITE_EX + "\nEnter new task priority: ").strip().lower()
                if not new_priority:
                    new_priority = task["priority"]
                if new_priority in PRIORITIES:
                    break      
                print(Fore.RED + "\nInvalid priority.\n")
            task["task"] = new_task
            task["priority"] = new_priority
            print(Fore.GREEN + f"Task changed to '{new_task}', priority changed to '{new_priority}'.")
            save_tasks(tasks)
        else:
            print(Fore.RED + "Invalid Task number")
    except ValueError:
        print(Fore.RED + "Invalid choice. Enter valid number.")

# Remove existing task from the json file then save it. 
def remove_task(tasks: list):
    if not tasks:
        print(Fore.RED + "No tasks to remove.")
        return
    view_tasks(tasks)
    
    try:
        task_index = int(input(Fore.LIGHTWHITE_EX + "\nEnter task's number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(Fore.GREEN + f"Task '{removed_task["task"]}' removed.")
        else:
            print(Fore.RED + "Invalid Task number")
    except ValueError:
        print(Fore.RED + "Invalid choice. Enter valid number.")

# Change existing task status then save it. 
def complete_task(tasks: list):
    if not tasks:
        print(Fore.RED + "No tasks to complete.")

    view_tasks(tasks)
    try:
        task_index = int(input(Fore.LIGHTWHITE_EX + "\nEnter task's number to complete: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            task["completed"] = True
            save_tasks(tasks)
            print(Fore.GREEN + f"Task '{task["task"]}' completed.")
        else:
            print(Fore.RED + "\nInvalid Task number")
    except ValueError:
        print(Fore.RED + "Invalid choice. Enter valid number.")

# Show program options menu
def show_menu():
    print(Fore.MAGENTA + "\nWelcome to python todo list!\n")
    print(Fore.BLUE + "1. View Tasks")
    print(Fore.GREEN + "2. Add Task")
    print(Fore.LIGHTMAGENTA_EX + "3. Edit Task")
    print(Fore.LIGHTRED_EX + "4. Remove Tasks")
    print(Fore.YELLOW + "5. Mark Task as completed")
    print(Fore.CYAN + "6. Search Tasks")
    print(Fore.RED + "7. exit")


# Main function
def main():
  tasks = load_tasks()

  while True:
    show_menu()
    print("\n")
    choice = input(Fore.LIGHTWHITE_EX + "Enter your choice: ").strip().lower()
    print(Style.RESET_ALL)

    if choice == "1":
      view_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        edit_task(tasks)
    elif choice == "4":
        remove_task(tasks)
    elif choice == "5":
        complete_task(tasks)
    elif choice == "6":
        search_tasks(tasks)
    elif choice == "7":
        print(Fore.LIGHTYELLOW_EX +"Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid Choice.")
    


if __name__ == "__main__":
    main()
