import uuid
import random
from datetime import datetime, timedelta

def generate_tasks(projects, sections, users):
    tasks = []
    now = datetime.now()

    for project in projects:
        project_sections = [
            s for s in sections if s["project_id"] == project["project_id"]
        ]

        n_tasks = random.randint(20, 60)

        for _ in range(n_tasks):
            section = random.choice(project_sections)

            tasks.append({
                "task_id": str(uuid.uuid4()),
                "project_id": project["project_id"],
                "section_id": section["section_id"],
                "created_at": now - timedelta(days=random.randint(0, 180))
            })

    return tasks

