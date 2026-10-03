import json, os
from datetime import datetime


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


def update_task():
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
    
    #Updates requested task from list
    updated_task = input("Enter name or ID of task you wish to update: ").lower()
    found = False
    for i in task_list:
        if i["description"].lower() == updated_task or str(i["id"]) == updated_task:
            i["description"] = input("Enter new name for task: ")
            i["updatedAt"] = datetime.now().isoformat()
            found = True

    if not found:
        print("No task with corresponding name or ID")
        return
    
    #Updates JSON with new list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Task updated successfully")


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
    deleted_task = input("Enter name or ID of task you wish to delete: ").lower()
    found = False
    for i in task_list:
        if i["description"].lower() == deleted_task or str(i["id"]) == deleted_task:
            task_list.remove(i)
            found = True

    if not found:
        print("No task with corresponding name or ID")
        return
    
    #Updates JSON with new list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Task deleted successfully")


def mark_in_progress():
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
    
    #Marks task as in progress
    updated_task = input("Enter name or ID of task you wish to mark as in progress: ").lower()
    found = False
    for i in task_list:
        if i["description"].lower() == updated_task or str(i["id"]) == updated_task:
            i["status"] = "in-progress"
            i["updatedAt"] = datetime.now().isoformat()
            found = True

    if not found:
        print("No task with corresponding name or ID")
        return
    
    #Updates JSON with new list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Task successfully marked as in progress")


def mark_done():
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
    
    #Marks task as done
    updated_task = input("Enter name or ID of task you wish to mark as done: ").lower()
    found = False
    for i in task_list:
        if i["description"].lower() == updated_task or str(i["id"]) == updated_task:
            i["status"] = "done"
            i["updatedAt"] = datetime.now().isoformat()
            found = True

    if not found:
        print("No task with corresponding name or ID")
        return
    
    #Updates JSON with new list
    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Task successfully marked as done")


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


def list_todo():
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
    found = False
    for i in task_list:
        if i["status"] == "to-do":
            print(f"{num}. {i["description"]}")
            found = True
            num+=1
    
    if not found:
        print("No tasks to do")


def list_in_progress():
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
    found = False
    for i in task_list:
        if i["status"] == "in-progress":
            print(f"{num}. {i["description"]}")
            found = True
            num+=1
    
    if not found:
        print("No tasks in progress")


def list_done():
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
    found = False
    for i in task_list:
        if i["status"] == "done":
            print(f"{num}. {i["description"]}")
            found = True
            num+=1
    
    if not found:
        print("No tasks done")

add_task()
update_task()
mark_done()
list_task()