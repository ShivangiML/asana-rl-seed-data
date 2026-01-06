import uuid
import random
from datetime import datetime, timedelta

# --------------------
# Task name templates
# --------------------

ENGINEERING_TASKS = [
    "Fix {component} bug",
    "Refactor {component} module",
    "Add tests for {component}",
    "Investigate {component} issue",
    "Optimize {component} performance"
]

MARKETING_TASKS = [
    "Draft copy for {campaign}",
    "Design assets for {campaign}",
    "Schedule posts for {campaign}",
    "Review campaign metrics"
]

GENERIC_TASKS = [
    "Weekly sync",
    "Follow up on action items",
    "Update documentation",
    "Prepare status update"
]

COMPONENTS = ["auth", "payments", "dashboard", "API"]
CAMPAIGNS = ["Q2 launch", "Webinar", "Email campaign"]

# --------------------
# Helpers
# --------------------

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


def generate_due_date(created_at):
    """
    Distribution:
    - 10% no due date
    - 25% within 1 week
    - 40% within 1 month
    - 20% within 1–3 months
    - 5% overdue
    """
    r = random.random()

    if r < 0.10:
        return None
    elif r < 0.35:
        days = random.randint(1, 7)
    elif r < 0.75:
        days = random.randint(8, 30)
    elif r < 0.95:
        days = random.randint(31, 90)
    else:
        days = -random.randint(1, 14)

    due = created_at + timedelta(days=days)

    # Avoid weekends 85% of the time
    if random.random() < 0.85:
        while due.weekday() >= 5:
            due += timedelta(days=1)

    return due


def generate_completion(created_at):
    """
    Returns (completed, completed_at)
    """
    completed = random.random() < 0.65

    if not completed:
        return False, None

    completed_at = created_at + timedelta(
        days=random.randint(1, 21)
    )

    if completed_at > datetime.now():
        completed_at = datetime.now()

    return True, completed_at


# --------------------
# Main generator
# --------------------

def generate_tasks(projects, sections, users):
    tasks = []
    now = datetime.now()

    for project in projects:
        project_sections = [
            s for s in sections if s["project_id"] == project["project_id"]
        ]

        # Non-uniform task count per project
        n_tasks = random.randint(20, 60)

        for _ in range(n_tasks):
            section = random.choice(project_sections)
            created_at = now - timedelta(days=random.randint(0, 180))

            # 15% unassigned
            assignee_id = None
            if random.random() > 0.15:
                assignee_id = random.choice(users)["user_id"]

            due_date = generate_due_date(created_at)
            completed, completed_at = generate_completion(created_at)

            tasks.append({
                "task_id": str(uuid.uuid4()),
                "project_id": project["project_id"],
                "section_id": section["section_id"],
                "assignee_id": assignee_id,
                "name": generate_task_name(project["name"]),
                "due_date": due_date,
                "completed": completed,
                "completed_at": completed_at,
                "created_at": created_at
            })

    return tasks
