"""View all tasks from tasks.json."""

from datetime import datetime


def view_tasks(tasks, sort_by=None):
    """Logic for displaying tasks."""
    if not tasks:
        print("No tasks found.")
        return

    if sort_by == "due_date":
        sorted_tasks = sorted(
            tasks.items(),
            key=lambda task: (
                datetime.strptime(task[1]["due_date"], "%Y-%m-%d")
                if task[1]["due_date"]
                else datetime.max
            ),
        )
    elif sort_by == "priority":
        sorted_tasks = sorted(tasks.items(), key=lambda task: task[1]["priority"])
    elif sort_by == "status":
        sorted_tasks = sorted(
            tasks.items(), key=lambda task: task[1].get("completed", False)
        )
    else:
        sorted_tasks = tasks.items()
    print(f"Current Tasks (sorted by {sort_by if sort_by else 'default order'}):")
    for title, details in sorted_tasks:
        status = "Completed" if details.get("completed", False) else "Incomplete"
        print(
            f"\nTitle: {title}\n"
            f"Description: {details['description']}\n"
            f"Due Date: {details['due_date']}\n"
            f"Priority: {details['priority']}\n"
            f"Status: {status}"
        )
