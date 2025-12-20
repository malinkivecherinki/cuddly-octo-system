#!/usr/bin/env python3
"""
TaskFlow Manager - Task management system with workflow automation.
"""

from datetime import datetime
from typing import List, Dict, Optional

class Task:
    """Represents a single task."""
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.status = "pending"
        self.created_at = datetime.now()
        self.completed_at = None
    
    def complete(self):
        """Mark task as completed."""
        self.status = "completed"
        self.completed_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }

class TaskFlow:
    """Main task management class."""
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task."""
        task = Task(title, description)
        self.tasks.append(task)
        return task
    
    def get_pending_tasks(self) -> List[Task]:
        """Get all pending tasks."""
        return [task for task in self.tasks if task.status == "pending"]
    
    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return [task for task in self.tasks if task.status == "completed"]

if __name__ == "__main__":
    flow = TaskFlow()
    flow.add_task("Setup project", "Initialize the project structure")
    flow.add_task("Write documentation", "Create README and API docs")
    
    print(f"Total tasks: {len(flow.tasks)}")
    print(f"Pending: {len(flow.get_pending_tasks())}")
