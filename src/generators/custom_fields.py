import uuid
import random

CUSTOM_FIELDS = [
    {
        "name": "Priority",
        "type": "enum",
        "values": ["High", "Medium", "Low"]
    },
    {
        "name": "Effort",
        "type": "number",
        "values": ["1", "2", "3", "4", "5"]
    },
    {
        "name": "Status",
        "type": "enum",
        "values": ["On Track", "At Risk", "Blocked"]
    }
]

def generate_custom_field_definitions(projects):
    field_defs = []

    for project in projects:
        for field in CUSTOM_FIELDS:
            field_defs.append({
                "field_id": str(uuid.uuid4()),
                "project_id": project["project_id"],
                "name": field["name"],
                "field_type": field["type"]
            })

    return field_defs


def generate_custom_field_values(tasks, field_defs):
    values = []

    for task in tasks:
        task_fields = [
            f for f in field_defs if f["project_id"] == task["project_id"]
        ]

        for field in task_fields:
            if random.random() < 0.20:
                continue  # field left empty

            values.append({
                "task_id": task["task_id"],
                "field_id": field["field_id"],
                "value": random.choice(
                    next(
                        f["values"]
                        for f in CUSTOM_FIELDS
                        if f["name"] == field["name"]
                    )
                )
            })

    return values
