"""View all tasks from tasks.json."""


def view_tasks(tasks):
    """Logic for displaying tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("Current Tasks:")
    for title, details in tasks.items():
        status = "Completed" if details.get("completed", False) else "Incomplete"
        print(
            f"\nTitle: {title}\n"
            f"Description: {details['description']}\n"
            f"Due Date: {details['due_date']}\n"
            f"Priority: {details['priority']}\n"
            f"Status: {status}"
        )
