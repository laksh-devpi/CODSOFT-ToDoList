import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    print("\n========== YOUR TASKS ==========\n")

    for i, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task["completed"] else "⏳ Pending"
        print(f"{i}. {task['title']} - {status}")

    print()


def add_task(tasks):
    title = input("\nEnter the task: ").strip()

    if title == "":
        print("❌ Task cannot be empty.\n")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("✅ Task added successfully!\n")


def complete_task(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to mark as completed: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed.\n")
        else:
            print("❌ Invalid task number.\n")

    except ValueError:
        print("❌ Please enter a valid number.\n")


def delete_task(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"🗑️ '{removed['title']}' deleted successfully.\n")
        else:
            print("❌ Invalid task number.\n")

    except ValueError:
        print("❌ Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=" * 40)
        print("       TO-DO LIST MANAGER")
        print("=" * 40)

        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\n👋 Thank you for using To-Do List Manager!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()