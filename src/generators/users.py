import uuid
import random
from datetime import datetime, timedelta

ROLES = [
    ("Engineer", 0.45),
    ("Product Manager", 0.10),
    ("Designer", 0.07),
    ("Marketing", 0.10),
    ("Sales Ops", 0.08),
    ("People Ops", 0.05),
    ("Manager", 0.10),
    ("Director", 0.05),
]

def weighted_choice(choices):
    r = random.random()
    upto = 0
    for role, weight in choices:
        upto += weight
        if upto >= r:
            return role
    return choices[-1][0]

def generate_users(n_users):
    users = []
    start_date = datetime.now() - timedelta(days=3*365)

    for _ in range(n_users):
        users.append({
            "user_id": str(uuid.uuid4()),
            "role": weighted_choice(ROLES),
            "created_at": start_date + timedelta(days=random.randint(0, 3*365))
        })

    return users
