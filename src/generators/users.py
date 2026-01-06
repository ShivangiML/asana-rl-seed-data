import uuid
import random
from datetime import datetime, timedelta

FIRST_NAMES = [
    "Aarav", "Emily", "Liam", "Sophia", "Noah", "Olivia",
    "Arjun", "Isabella", "Ethan", "Mia", "Lucas", "Amelia",
    "Rohan", "Ava", "Daniel", "Charlotte", "James", "Harper"
]

LAST_NAMES = [
    "Patel", "Smith", "Johnson", "Brown", "Khan", "Garcia",
    "Lee", "Martinez", "Nguyen", "Singh", "Taylor", "Anderson"
]

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

def generate_users(n_users, company_domain="acme.com"):
    users = []
    start_date = datetime.now() - timedelta(days=3*365)

    for _ in range(n_users):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        email = f"{first.lower()}.{last.lower()}@{company_domain}"

        users.append({
            "user_id": str(uuid.uuid4()),
            "organization_id": "org_001",
            "full_name": f"{first} {last}",
            "email": email,
            "role": weighted_choice(ROLES),
            "created_at": start_date + timedelta(days=random.randint(0, 3*365))
        })

    return users
