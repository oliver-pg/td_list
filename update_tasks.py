"""Add 'completed' field to tasks in tasks.json if missing."""

import json


def update_tasks():
    """Logic for updating marked tasks."""
    try:
        with open("tasks.json", "r", encoding="utf-8") as json_file:
            tasks = json.load(json_file)

        # Add 'completed', don't overwrite existing mark
        for task in tasks.values():
            if "completed" not in task:
                task["completed"] = False

        # Save updated tasks
        with open("tasks.json", "w", encoding="utf-8") as json_file:
            json.dump(tasks, json_file, indent=4)

        print("All tasks updated with 'completed' field.")
    except FileNotFoundError:
        print("tasks.json not found. No update needed.")
