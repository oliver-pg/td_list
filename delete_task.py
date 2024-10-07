"""Delete a task in tasks.json."""

import json


def delete_task(tasks):
    """Logic for deleting tasks."""
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

        confirm = (
            input(f"Are you sure you want to delete '{task_title}'? (y/n): ")
            .strip()
            .lower()
        )

        if confirm == "y":
            del tasks[task_title]
            print(f"Task '{task_title}' deleted.")
        elif confirm == "n":
            print("Task deletion canceled.")
        else:
            print("Invalid input. Task deletion canceled.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid task number. Please try again.")
    except KeyError:
        print("Error: Task not found.")
    except Exception as err:
        print(f"Unexpected error: {err}")

    # Attempt to save the updated tasks to tasks.json
    try:
        with open("tasks.json", "w", encoding="utf-8") as json_file:
            json.dump(tasks, json_file, indent=4)
        print("Tasks updated successfully.")
    except IOError as err:
        print(f"Error saving tasks: {err}")
