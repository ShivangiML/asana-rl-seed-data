import uuid
import random

TAG_NAMES = [
    "urgent", "backend", "frontend", "design",
    "bug", "tech-debt", "launch", "follow-up"
]

def generate_tags(organization_id):
    tags = []

    for name in TAG_NAMES:
        tags.append({
            "tag_id": str(uuid.uuid4()),
            "organization_id": organization_id,
            "name": name
        })

    return tags


def generate_task_tags(tasks, tags):
    task_tags = []

    for task in tasks:
        if random.random() < 0.50:
            continue

        n_tags = random.randint(1, 2)

        for tag in random.sample(tags, n_tags):
            task_tags.append({
                "task_id": task["task_id"],
                "tag_id": tag["tag_id"]
            })

    return task_tags
