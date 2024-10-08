"""Manage all tasks in the console application."""

from load_tasks import load_tasks
from update_tasks import update_tasks
from view_tasks import view_tasks
from add_task import add_task
from mark_task import mark_task
from delete_task import delete_task
from save_tasks import save_tasks


def display_menu():
    """Display the task manager menu."""
    print("\nTask Manager Menu:")
    print("1. [View Tasks]")
    print("2. [View Tasks (Sorted)]")
    print("3. [Add Task]")
    print("4. [Mark Task Complete]")
    print("5. [Delete Task]")
    print("6. [Exit]")


def handle_sorting(tasks):
    """Handle the sorting of tasks."""
    sort_choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

    if sort_choice == "1":
        view_tasks(tasks)
    elif sort_choice == "2":
        sort_choice = input("Sort by: 1. Due Date 2. Priority 3. Status: ").strip()
        if sort_choice == "1":
            view_tasks(tasks, sort_by="due_date")
        elif sort_choice == "2":
            view_tasks(tasks, sort_by="priority")
        elif sort_choice == "3":
            view_tasks(tasks, sort_by="status")
        else:
            print("Invalid choice.")


def manage_tasks():
    """Logic for managing tasks (view, add, mark complete, delete)."""
    try:
        tasks = load_tasks()
    except FileNotFoundError:
        tasks = {}

    # Auto update tasks with 'completed' field if missing
    update_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            handle_sorting(tasks)
        elif choice == "3":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            print("Exiting task manager.")
            save_tasks(tasks)
            return
        else:
            print("Invalid choice, please select again.")
