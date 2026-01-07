import uuid
import random
from datetime import timedelta

COMMENT_TEMPLATES = [
    "Can you take a look at this?",
    "This is blocked right now.",
    "I’ve pushed a fix for this.",
    "Waiting on feedback from the team.",
    "Looks good to me 👍",
    "Let’s discuss this in the next sync.",
    "Any updates on this?",
    "This should be ready by EOD.",
    "Following up on this task."
]

def generate_comments(tasks, users):
    comments = []

    for task in tasks:
        # Not all tasks have comments
        if random.random() < 0.30:
            continue

        n_comments = random.randint(1, 5)

        for _ in range(n_comments):
            author = random.choice(users)

            created_at = task["created_at"] + timedelta(
                days=random.randint(0, 14)
            )

            # Comments should not be after completion
            if task.get("completed_at") and created_at > task["completed_at"]:
                created_at = task["completed_at"]

            comments.append({
                "comment_id": str(uuid.uuid4()),
                "task_id": task["task_id"],
                "user_id": author["user_id"],
                "body": random.choice(COMMENT_TEMPLATES),
                "created_at": created_at
            })

    return comments
