"""Delete a task in tasks.json."""

import json


def delete_task(tasks):
    """Logic for deleted tasks."""
    if not tasks:
        print("No tasks available to delete.")
        return

    print("Delete a task:")
    for i, title in enumerate(tasks, 1):
        print(f"{i}. {title}")

    task_num = input("Enter the number of the task to delete: ").strip()

    try:
        task_index = int(task_num) - 1
        task_title = list(tasks.keys())[task_index]
        confirm = input(
            f"Are you sure you want to delete '{task_title}'? (y/n): "
        ).strip()

        if confirm == "y":
            del tasks[task_title]
            print(f"Task '{task_title}' deleted.")
        else:
            print("Task deletion canceled.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

    with open("tasks.json", "w", encoding="utf-8") as json_file:
        json.dump(tasks, json_file, indent=4)
