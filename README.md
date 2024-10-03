# Task Tracker CLI
Task tracker CLI application, details can be found on [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## How to Run

The numbers in the commands below correspond to the task's ID number

Clone the repository and run the following command:

```bash
git clone https://github.com/Cbooch13/task-tracker-cli.git
cd task-tracker-cli
```

### Add a task
```bash
python3 task-cli.py add "Sample description"
```

### Delete a task
```bash
python3 task-cli.py delete 1
```

### Update a task
```bash
python3 task-cli.py update 1 "Updated description"
```

### Mark a task's status (todo, in-progress, done)
```bash
python3 task-cli.py mark 1 in-progress
python3 task-cli.py mark 2 done
python3 task-cli.py mark 3 todo
```

### List tasks
```bash
#Lists all tasks
python3 task-cli.py list

#Filters by status
python3 task-cli.py list todo
python3 task-cli.py list in-progress
python3 task-cli.py list done
```







