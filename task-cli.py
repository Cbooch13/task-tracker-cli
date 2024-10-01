# Task tracker implemented in python run through the CLI.  Roadmap.sh project
# Caleb Bucci
# 2024-09-23

import argparse
import os
import json
from datetime import datetime

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


def add_task(desc: str):
    tasks = load_tasks()
    today = datetime.today().isoformat()
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



def mark_task(id: int, status: str):
    pass

def list_tasks(status: str):
    pass



def main():

    #Argument parser
    parser = argparse.ArgumentParser(
        prog = "task-cli",
        description = "Task Tracker CLI",
        epilog = "Program Usage : python3 task-cli filename.json"
    )

    subparsers = parser.add_subparsers(dest='action', required=True)

    # Add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Update a task
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("description",help="New description of the task")

    # Delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # Mark a task as in-progress or done
    parser_mark = subparsers.add_parser("mark", help="Mark a task as in-progress or done")
    parser_mark.add_argument("id", type=int, help="ID of the task to mark")
    parser_mark.add_argument("status", choices=["todo", "in-progress", "done"], 
                help="Status to set (todo, in-progress, done)")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", type=str, nargs='?', default = "all", 
                choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    
    #Parse args
    args = parser.parse_args()

    if args.action == 'add':
        add_task(args.description)
    elif args.action == 'update':
        update_task(args.id, args.description)
    elif args.action == 'delete':
        delete_task(args.id)
    elif args.action == 'mark':
        mark_task(args.id, args.status)
    elif args.action == 'list':
        list_tasks(args.status)


if __name__ == "__main__":
    main()