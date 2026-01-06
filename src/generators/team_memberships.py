import random

def generate_team_memberships(users, teams):
    memberships = []

    for user in users:
        team = random.choice(teams)
        memberships.append({
            "user_id": user["user_id"],
            "team_id": team["team_id"]
        })

    return memberships
