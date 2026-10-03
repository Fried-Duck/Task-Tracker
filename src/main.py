import json, os
from datetime import datetime

#Adds a new taks
def add_task():
    description = input("Enter task name: ")

    new_task = {
        "id": int(datetime.now().timestamp()),
        "description": description,
        "status": "to-do",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": "N/A"
    }

    #Looks for exisiting JSON and loads task list. If not found initializes new list.
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                task_list = json.load(f)
            except json.JSONDecodeError:
                task_list = []
    else:
        task_list = []

    #Adds task to list
    task_list.append(new_task)

    #Creates or overwrites JSON with new task list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print(f"Task added successfully (ID: {new_task["id"]})")



#Updates selected task
def update_task():
    pass

#Deletes selected task
def delete_task():
    #Looks for existing JSON and loads task list. If none available ends function.
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                task_list = json.load(f)
            except json.JSONDecodeError:
                print("No tasks remaining")
                return
    else:
        print("No tasks remaining")
        return
    
    #Removes requested task from list
    deleted_task = input("What ")
    task_list.remove()
    
    #Updates JSON with new list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Task deleted successfully")

def list_task():
    #Looks for existing JSON and loads task list. If none available ends function.
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                task_list = json.load(f)
            except json.JSONDecodeError:
                print("No tasks remaining")
                return
    else:
        print("No tasks remaining")
        return
    
    num=1
    for i in task_list:
        print(f"{num}. {i["description"]}")
        num+=1

list_task()