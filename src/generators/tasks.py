import uuid
import random
from datetime import datetime, timedelta

ENGINEERING_TASKS = [
    "Fix {component} bug",
    "Refactor {component} module",
    "Add tests for {component}",
    "Investigate {component} issue"
]

MARKETING_TASKS = [
    "Draft copy for {campaign}",
    "Design assets for {campaign}",
    "Schedule posts for {campaign}"
]

GENERIC_TASKS = [
    "Weekly sync",
    "Follow up on action items",
    "Update documentation"
]

COMPONENTS = ["auth", "payments", "dashboard", "API"]
CAMPAIGNS = ["Q2 launch", "Webinar", "Email campaign"]

def generate_task_name(project_name):
    if "Sprint" in project_name or "Bug" in project_name:
        return random.choice(ENGINEERING_TASKS).format(
            component=random.choice(COMPONENTS)
        )
    elif "Campaign" in project_name:
        return random.choice(MARKETING_TASKS).format(
            campaign=random.choice(CAMPAIGNS)
        )
    else:
        return random.choice(GENERIC_TASKS)

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

            assignee = None
            if random.random() > 0.15:  # 85% assigned
                assignee = random.choice(users)["user_id"]

            tasks.append({
                "task_id": str(uuid.uuid4()),
                "project_id": project["project_id"],
                "section_id": section["section_id"],
                "name": generate_task_name(project["name"]),
                "assignee_id": assignee,
                "created_at": now - timedelta(days=random.randint(0, 180))
            })

    return tasks
