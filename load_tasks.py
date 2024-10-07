"""Load task information from tasks.json through task_manager.py."""

import json
import os


def load_tasks():
    """Logic for loading tasks."""
    tasks = {}
    try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r", encoding="utf-8") as json_file:
                tasks = json.load(json_file)
        else:
            print("No task file found, starting with an empty task list.")
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        tasks = {}
    except IOError as err:
        print(f"File error: {err}")
        tasks = {}
    return tasks
