"""Edit an existing task in tasks.json through task_manager.py."""


def edit_task(tasks):
    """Logic for editing an existing task."""
    if not tasks:
        print("No tasks available to edit.")
        return

    print("edit a task:")
    for i, title in enumerate(tasks, 1):
        print(f"{i}. {title}")

    task_num = input("Enter the number of the task to edit: ").strip()

    try:
        task_index = int(task_num) - 1
        task_title = list(tasks.keys())[task_index]
        task_details = tasks[task_title]

        print("\nWhat would you like to edit?")
        print("1. [Title]")
        print("2. [Description]")
        print("3. [Due Date]")
        print("4. [Priority]")

        edit_choice = input("Enter your choice (1/2/3/4): ").strip()

        if edit_choice == "1":
            new_title = input(f"Enter new title (current: {task_title}): ").strip()
            tasks[new_title] = tasks.pop(task_title)
            print(f"Task title updated to '{new_title}'.")
        elif edit_choice == "2":
            new_description = input(
                f"Enter new description (current: {task_details['description']}): "
            ).strip()
            tasks[task_title]["description"] = new_description
            print("Task priority updated.")
        elif edit_choice == "3":
            new_due_date = input(
                f"Enter new due date (current: {task_details['due_date']}): "
            ).strip()
            tasks[task_title]["due_date"] = new_due_date
            print("Task due date updated.")
        elif edit_choice == "4":
            new_priority = input(
                f"Enter new priority (current: {task_details['priority']}): "
            ).strip()
            tasks[task_title]["priority"] = new_priority
            print("Task priority updated.")
        else:
            print("Invalid choice. No changes were made.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")
