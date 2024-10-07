"""Load task information from tasks.json through task_manager.py."""

import json


def load_tasks():
    """Logic for loading tasks."""
    try:
        with open("tasks.json", "r", encoding="utf-8") as json_file:
            tasks = json.load(json_file)
    except FileNotFoundError:
        tasks = {}

    return tasks
