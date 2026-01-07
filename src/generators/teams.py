from datetime import datetime, timedelta
import random
import uuid

def generate_teams(organization_id):
    teams = []
    start_date = datetime(2021, 1, 1)

    TEAM_DEPARTMENTS = {
        "Engineering": ["Backend", "Frontend", "Infra", "Mobile"],
        "Product": ["Product Management", "Design"],
        "Marketing": ["Growth", "Content", "SEO"],
        "Operations": ["HR", "Finance", "IT"]
    }

    for dept, team_names in TEAM_DEPARTMENTS.items():
        for name in team_names:
            teams.append({
                "team_id": str(uuid.uuid4()),
                "organization_id": organization_id,
                "name": name,
                "department": dept,
                "created_at": start_date + timedelta(days=random.randint(0, 900))
            })

    return teams
