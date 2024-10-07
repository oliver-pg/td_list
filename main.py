"""Main file for code execution."""

import task_manager


def main():
    """Execute code here and manage your tasks with task_manager.py."""
    while True:
        if not task_manager.manage_tasks():
            break


if __name__ == "__main__":
    main()
