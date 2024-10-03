# Task tracker implemented in python run through the CLI.  Roadmap.sh project
# Caleb Bucci
# 2024-09-23

import argparse
import actions

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
    parser_list.add_argument("status", type=str, nargs='?', 
                choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    
    #Parse args
    args = parser.parse_args()

    if args.action == 'add':
        actions.add_task(args.description)
    elif args.action == 'update':
        actions.update_task(args.id, args.description)
    elif args.action == 'delete':
        actions.delete_task(args.id)
    elif args.action == 'mark':
        actions.mark_task(args.id, args.status)
    elif args.action == 'list':
        actions.list_tasks(args.status)


if __name__ == "__main__":
    main()