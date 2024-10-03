import os
import json
from datetime import datetime
from tabulate import tabulate


TASKS_FILE = 'tasks.json'

#Loads tasks from json file into dict
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    else:
        return []
    
    
#Saves dict into json file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        file.write(json.dumps(tasks, indent=4))

#Adds task to json
def add_task(desc: str):
    tasks = load_tasks()
    today = datetime.today().isoformat()
    #Determines id of new item, either 1 if no tasks or highest existing id + 1
    id = 1
    if len(tasks) > 0:
        id += max(task['id'] for task in tasks)

    new_task = {
        "id" : id,
        "description" : desc,
        "status" : "todo",
        "createdAt" : today,
        "updatedAt" : today
    }
    tasks.append(new_task)
    save_tasks(tasks)
    
#Deletes task from json
def delete_task(id: int):
    tasks = load_tasks()
    removed = False
    for task in tasks:
        if task['id'] == id:
            removed = True
            tasks.remove(task)
            break
    
    if not removed:
        print("Task ID " + str(id) + " not found.")
    save_tasks(tasks)
    
#Updates task description
def update_task(id: int, desc: str):
    tasks = load_tasks()
    updated = False
    for task in tasks:
        if task['id'] == id:
            updated = True
            task['description'] = desc
            task['updatedAt'] = datetime.today().isoformat()
            break
    
    if not updated:
        print("Task ID " + str(id) + " not found.")
    save_tasks(tasks)

#Marks task to {todo, in-progress, done}
def mark_task(id: int, status: str):
    tasks = load_tasks()
    updated = False
    for task in tasks:
        if task['id'] == id:
            updated = True
            task['status'] = status
            break
    
    if not updated:
        print("Task ID " + str(id) + " not found.")
    save_tasks(tasks)

# Lists tasks based on status
def list_tasks(status: str):
    tasks = load_tasks()
    
    if status:
        filtered = []
        for task in tasks:
            if task['status'] == status:
                filtered.append(task)
        tasks = filtered
    
    #Tabulates the data for output
    table = tabulate(tasks, headers="keys")
    print(table)