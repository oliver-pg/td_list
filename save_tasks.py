"""Save tasks to tasks.json"""

import json


def save_tasks(tasks):
    """Save the state of tasks."""
    with open("tasks.json", "w", encoding="utf-8") as json_file:
        json.dump(tasks, json_file, indent=4)
