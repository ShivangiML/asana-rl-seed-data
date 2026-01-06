import uuid

DEFAULT_SECTIONS = [
    "Backlog",
    "To Do",
    "In Progress",
    "Review",
    "Done"
]

def generate_sections(projects):
    sections = []

    for project in projects:
        for name in DEFAULT_SECTIONS:
            sections.append({
                "section_id": str(uuid.uuid4()),
                "project_id": project["project_id"],
                "name": name
            })

    return sections
