"""Add a task to tasks.json with a title and relevant details through task_manager.py."""

import json


def add_task(tasks):
    """Logic for adding tasks."""
    new_task_title = input("Enter task title: ")
    new_task_details = {
        "description": input("Enter task description: "),
        "due_date": input("Enter due date: "),
        "priority": input("Enter task priority: "),
    }

    tasks[new_task_title] = new_task_details

    with open("tasks.json", "w", encoding="utf-8") as json_file:
        json.dump(tasks, json_file, indent=4)

    print(f"Task '{new_task_title}' added successfully.")
