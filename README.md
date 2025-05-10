https://roadmap.sh/projects/task-tracker

# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. This tool helps you keep track of what you need to do, what you're currently working on, and what you've completed.

## Features

- Add, update, and delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status (todo, in-progress, done)
- Tasks are stored in a local JSON file
- Simple and intuitive command-line interface

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd task-tracker
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The Task Tracker CLI supports the following commands:

### Adding Tasks
```bash
python task_cli.py add "Your task description"
```

### Updating Tasks
```bash
python task_cli.py update <task_id> "New task description"
```

### Deleting Tasks
```bash
python task_cli.py delete <task_id>
```

### Marking Task Status
```bash
python task_cli.py mark-in-progress <task_id>
python task_cli.py mark-done <task_id>
```

### Listing Tasks
```bash
python task_cli.py list               
python task_cli.py list todo            
python task_cli.py list in-progress      
python task_cli.py list done              
```

## Task Properties

Each task has the following properties:
- `id`: Unique identifier
- `description`: Task description
- `status`: Current status (todo, in-progress, done)
- `createdAt`: Creation timestamp
- `updatedAt`: Last update timestamp

## Development

This project is built using:
- Python 3.x
- Standard library modules (no external dependencies)

## License

MIT License
