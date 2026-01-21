import json

file = 'tasks.json'

def load_items():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {"tasks": []}

def save_task(tasks):
    try:
        with open(file, "w") as f:
            json.dump(tasks, f)
    except:
        print("Error saving tasks.")

def create_task(tasks):
    desc = input("Enter task description: ").strip()
    if desc:
        tasks["tasks"].append({"description": desc, "completed": False})
        save_task(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

def mark_as_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_task(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks["tasks"], start=1):
            status = "Done" if task["completed"] else "[Pending]"
            print(f"{idx}. {task['description']} - {status}")

def main():
    tasks = load_items()

    while True:
        print("\n--- Task Manager ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Save and Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_as_complete(tasks)
        elif choice == '4':
            save_task(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
