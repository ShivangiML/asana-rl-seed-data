import uuid
import random
from datetime import datetime, timedelta

PROJECT_TEMPLATES = {
    "Engineering": [
        "Sprint {n} - {team}",
        "Bug Bash - {team}",
        "Tech Debt Cleanup - {team}"
    ],
    "Marketing": [
        "Q{q} Campaign Launch",
        "Content Calendar - {month}",
        "Product Launch - {product}"
    ],
    "Product": [
        "Roadmap Planning Q{q}",
        "Feature Discovery - {area}"
    ],
    "People Ops": [
        "Hiring Plan Q{q}",
        "Onboarding Improvements"
    ]
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
PRODUCTS = ["Analytics", "Payments", "Mobile App", "Dashboard"]
AREAS = ["Growth", "Core UX", "Platform"]

def generate_projects(teams, months_back=6):
    projects = []
    now = datetime.now()

    for team in teams:
        n_projects = random.randint(2, 6)

        for i in range(n_projects):
            template = random.choice(
                PROJECT_TEMPLATES.get(team["department"], ["General Work"])
            )

            name = template.format(
                n=i+1,
                team=team["name"],
                q=random.randint(1, 4),
                month=random.choice(MONTHS),
                product=random.choice(PRODUCTS),
                area=random.choice(AREAS)
            )

            created_at = now - timedelta(days=random.randint(0, months_back * 30))

            projects.append({
                "project_id": str(uuid.uuid4()),
                "team_id": team["team_id"],
                "name": name,
                "created_at": created_at
            })

    return projects
