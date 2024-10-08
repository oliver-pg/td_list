"""Filter tasks in tasks.json by status, priority or due date through task_manager.py."""

from datetime import datetime, timedelta


def task_due_soon(due_date):
    """Check if the task is due within the next 7 days."""
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        return datetime.now() <= due_date_obj <= datetime.now() + timedelta(days=7)
    except ValueError:
        return False


def task_overdue(due_date):
    """Check if the task is overdue."""
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        return due_date_obj < datetime.now()
    except ValueError:
        return False


def filter_tasks(tasks, filter_by=None):
    """Logic for filtering tasks."""
    filtered_tasks = tasks.items()

    if filter_by == "incomplete":
        filtered_tasks = {
            key: value
            for key, value in tasks.items()
            if not value.get("completed", False)
        }
    elif filter_by == "completed":  # Add filtering for completed tasks
        filtered_tasks = {
            key: value for key, value in tasks.items() if value.get("completed", False)
        }
    elif filter_by == "high_priority":
        filtered_tasks = {
            key: value
            for key, value in tasks.items()
            if value["priority"].lower() == "high"
        }
    elif filter_by == "due_soon":
        filtered_tasks = {
            key: value
            for key, value in tasks.items()
            if task_due_soon(value["due_date"])
        }
    elif filter_by == "overdue":
        filtered_tasks = {
            key: value
            for key, value in tasks.items()
            if task_overdue(value["due_date"])
        }

    return filtered_tasks
