#!/usr/bin/env python3

import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional

TASKS_FILE = "tasks.json"

class TaskTracker:
    def __init__(self):
        self.tasks: Dict[int, Dict] = {}
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from JSON file if it exists."""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                print("Error: Invalid JSON file. Creating new tasks file.")
                self.tasks = {}
        else:
            self.tasks = {}

    def save_tasks(self) -> None:
        """Save tasks to JSON file."""
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def get_next_id(self) -> int:
        """Get the next available task ID."""
        return max(self.tasks.keys(), default=0) + 1

    def add_task(self, description: str) -> int:
        """Add a new task."""
        task_id = self.get_next_id()
        now = datetime.now().isoformat()
        self.tasks[task_id] = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "createdAt": now,
            "updatedAt": now
        }
        self.save_tasks()
        return task_id

    def update_task(self, task_id: int, description: str) -> bool:
        """Update an existing task."""
        if task_id not in self.tasks:
            return False
        
        self.tasks[task_id]["description"] = description
        self.tasks[task_id]["updatedAt"] = datetime.now().isoformat()
        self.save_tasks()
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        if task_id not in self.tasks:
            return False
        
        del self.tasks[task_id]
        self.save_tasks()
        return True

    def mark_task_status(self, task_id: int, status: str) -> bool:
        """Mark a task's status."""
        if task_id not in self.tasks or status not in ["todo", "in-progress", "done"]:
            return False
        
        self.tasks[task_id]["status"] = status
        self.tasks[task_id]["updatedAt"] = datetime.now().isoformat()
        self.save_tasks()
        return True

    def list_tasks(self, status: Optional[str] = None) -> List[Dict]:
        """List tasks, optionally filtered by status."""
        if status is None:
            return list(self.tasks.values())
        return [task for task in self.tasks.values() if task["status"] == status]

def print_usage():
    """Print usage instructions."""
    print("Usage:")
    print("  python task_cli.py add \"Task description\"")
    print("  python task_cli.py update <task_id> \"New description\"")
    print("  python task_cli.py delete <task_id>")
    print("  python task_cli.py mark-in-progress <task_id>")
    print("  python task_cli.py mark-done <task_id>")
    print("  python task_cli.py list [todo|in-progress|done]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    tracker = TaskTracker()
    command = sys.argv[1].lower()

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Task description required")
                sys.exit(1)
            task_id = tracker.add_task(sys.argv[2])
            print(f"Task added successfully (ID: {task_id})")

        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and new description required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            if tracker.update_task(task_id, sys.argv[3]):
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Task {task_id} not found")

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            if tracker.delete_task(task_id):
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Error: Task {task_id} not found")

        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            if tracker.mark_task_status(task_id, "in-progress"):
                print(f"Task {task_id} marked as in progress")
            else:
                print(f"Error: Task {task_id} not found")

        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Task ID required")
                sys.exit(1)
            task_id = int(sys.argv[2])
            if tracker.mark_task_status(task_id, "done"):
                print(f"Task {task_id} marked as done")
            else:
                print(f"Error: Task {task_id} not found")

        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else None
            tasks = tracker.list_tasks(status)
            if not tasks:
                print("No tasks found")
            else:
                for task in tasks:
                    print(f"ID: {task['id']}")
                    print(f"Description: {task['description']}")
                    print(f"Status: {task['status']}")
                    print(f"Created: {task['createdAt']}")
                    print(f"Updated: {task['updatedAt']}")
                    print("-" * 50)

        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
            sys.exit(1)

    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 