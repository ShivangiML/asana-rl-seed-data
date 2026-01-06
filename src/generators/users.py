import uuid
import random
from datetime import datetime, timedelta

def generate_users(n_users):
    users = []
    start_date = datetime.now() - timedelta(days=3*365)

    for _ in range(n_users):
        users.append({
            "user_id": str(uuid.uuid4()),
            "created_at": start_date + timedelta(days=random.randint(0, 3*365))
        })

    return users
