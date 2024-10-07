"""Manage all tasks in the console application."""

from load_tasks import load_tasks
from update_tasks import update_tasks
from add_task import add_task
from mark_task import mark_task
from delete_task import delete_task


def manage_tasks():
    """Logic for managing tasks (view, add, mark complete, delete)."""

    # Auto update tasks with 'completed' field before managing
    update_tasks()

    try:
        tasks = load_tasks()
    except FileNotFoundError:
        tasks = {}

    while True:
        print("\nTask Manager Menu:")
        print("1. [View Tasks]")
        print("2. [Add Task]")
        print("3. [Mark Task Complete]")
        print("4. [Delete Task]")
        print("5. [Exit]")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            print("Current Tasks:")
            if tasks:
                for title, details in tasks.items():
                    status = (
                        "Completed" if details.get("completed", False) else "Incomplete"
                    )
                    print(
                        f"\nTitle: {title}\n"
                        f"Description: {details["description"]}\n"
                        f"Due Date: {details["due_date"]}\n"
                        f"Priority: {details["priority"]}\n"
                        f"Status: {status}"
                    )
            else:
                print("No tasks found.")
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting task manager.")
            return False
        else:
            print("Invalid choice, please select again.")
