import uuid
import random

TEAM_TYPES = {
    "Engineering": [
        "Backend Platform",
        "Frontend Web",
        "Mobile Apps",
        "Infrastructure",
        "QA Automation"
    ],
    "Product": [
        "Product Core",
        "Growth",
        "Platform PMs"
    ],
    "Design": [
        "UX Design",
        "Brand Design"
    ],
    "Marketing": [
        "Demand Gen",
        "Content Marketing",
        "Product Marketing"
    ],
    "Sales Ops": [
        "Sales Operations",
        "Revenue Analytics"
    ],
    "People Ops": [
        "Recruiting",
        "HR Operations"
    ]
}

def generate_teams(organization_id):
    teams = []

    for dept, team_names in TEAM_TYPES.items():
        for name in team_names:
            teams.append({
                "team_id": str(uuid.uuid4()),
                "organization_id": organization_id,
                "name": name,
                "department": dept
            })

    return teams
