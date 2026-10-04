# Task-Tracker
A simple command-line task manager written in Python. You can add, rename, delete, and track tasks. Tasks are saved in a local tasks.json file.

REQUIREMENTS
- Python 3.12 or newer
- No additional packages required

HOW TO RUN
Clone the repository and run the following command:
1. Clone the repository and run the following command:
```git clone https://github.com/Fried-Duck/Task-Tracker.git
cd Task-Tracker
```
2. Run: python3 main.py

MENU OPTIONS
1. Add a task
2. Update a task’s name
3. Delete a task
4. Mark a task as in progress
5. Mark a task as done
6. List all tasks
7. List to-do tasks
8. List in-progress tasks
9. List completed tasks
10. Exit

When updating, deleting, or changing a task’s status, enter its name or ID.

SAVING TASKS
The program creates tasks.json in the current folder when you add your first task. It stores each task’s ID, name, status, creation time, and last update time. Keep this file to keep your saved tasks.

https://roadmap.sh/projects/task-tracker