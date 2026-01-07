import uuid
import random
from datetime import timedelta

SUBTASK_TEMPLATES = [
    "Review work",
    "Make requested changes",
    "QA verification",
    "Update documentation",
    "Follow-up"
]

def generate_subtasks(tasks):
    subtasks = []

    for task in tasks:
        # ~35% of tasks get subtasks
        if random.random() > 0.35:
            continue

        n_subtasks = random.randint(1, 4)

        for _ in range(n_subtasks):
            created_at = task["created_at"] + timedelta(
                days=random.randint(0, 3)
            )

            subtasks.append({
                "task_id": str(uuid.uuid4()),
                "parent_task_id": task["task_id"],
                "project_id": task["project_id"],
                "section_id": task["section_id"],
                "name": random.choice(SUBTASK_TEMPLATES),
                "assignee_id": task["assignee_id"],
                "created_at": created_at,
                "due_date": task["due_date"],
                "completed": False,
                "completed_at": None
            })

    return subtasks
