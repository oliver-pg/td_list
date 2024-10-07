"""Mark a task in tasks.json as complete."""

import json


def mark_task(tasks):
    """Logic for marking tasks as complete."""
    if not tasks:
        print("No tasks available to mark as complete.")
        return

    print("Mark a task as complete:")
    for i, title in enumerate(tasks, 1):
        print(
            f"{i}:. {title} - {'Completed' if tasks[title].get("completed", False) else 'Incomplete'}"
        )

    task_num = input("Enter the number of the task to mark as complete: ").strip()

    try:
        task_index = int(task_num) - 1
        task_title = list(tasks.keys())[task_index]
        # Mark as complete
        tasks[task_title]["completed"] = True
        print(f"Task '{task_title}' marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

        # Save marked tasks
        with open("tasks.json", "w", encoding="utf-8") as json_file:
            json.dump(tasks, json_file, indent=4)
