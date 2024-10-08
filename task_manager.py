"""Manage all tasks in the console application."""

from load_tasks import load_tasks
from update_tasks import update_tasks
from view_tasks import view_tasks
from filter_tasks import filter_tasks
from add_task import add_task
from edit_task import edit_task
from mark_task import mark_task
from delete_task import delete_task
from save_tasks import save_tasks


def display_menu():
    """Display the task manager menu."""
    print("\nTask Manager Menu:")
    print("1. [View Tasks]")
    print("2. [View Tasks (Sorted)]")
    print("3. [Filter Tasks]")
    print("4. [Add Task]")
    print("5. [Edit Task]")
    print("6. [Mark Task Complete]")
    print("7. [Delete Task]")
    print("8. [Exit]")


def handle_sorting(tasks):
    """Handle the sorting of tasks."""
    sort_choice = input("Sort by: 1. Due Date 2. Priority 3. Status: ").strip()

    if sort_choice == "1":
        view_tasks(tasks, sort_by="due_date")
    elif sort_choice == "2":
        view_tasks(tasks, sort_by="priority")
    elif sort_choice == "3":
        view_tasks(tasks, sort_by="status")
    else:
        print("Invalid choice.")


def handle_filtering(tasks):
    """Handle the filtering of tasks."""
    filter_choice = input(
        "\nFilter by: 1. Incomplete 2. Completed 3. High Priority 4. Due Soon 5. Overdue: "
    ).strip()

    if filter_choice == "1":
        filtered_tasks = filter_tasks(tasks, filter_by="incomplete")
    elif filter_choice == "2":  # Filter by completed tasks
        filtered_tasks = filter_tasks(tasks, filter_by="completed")
    elif filter_choice == "3":
        filtered_tasks = filter_tasks(tasks, filter_by="high_priority")
    elif filter_choice == "4":
        filtered_tasks = filter_tasks(tasks, filter_by="due_soon")
    elif filter_choice == "5":
        filtered_tasks = filter_tasks(tasks, filter_by="overdue")
    else:
        print("Invalid choice.")
        return

    view_tasks(filtered_tasks)


def manage_tasks():
    """Logic for managing tasks (view, add, edit, mark complete, delete)."""
    try:
        tasks = load_tasks()
    except FileNotFoundError:
        tasks = {}

    # Auto update tasks with 'completed' field if missing
    update_tasks()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4/5/6/7/8): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            handle_sorting(tasks)
        elif choice == "3":  # Filter Tasks now handled as option 3
            handle_filtering(tasks)
        elif choice == "4":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            mark_task(tasks)
            save_tasks(tasks)
        elif choice == "7":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "8":
            print("Exiting task manager.")
            save_tasks(tasks)
            return
        else:
            print("Invalid choice, please select again.")
