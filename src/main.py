import sqlite3
from pathlib import Path

# Generators
from generators.users import generate_users
from generators.teams import generate_teams
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.subtasks import generate_subtasks
from generators.comments import generate_comments
from generators.custom_fields import (
    generate_custom_field_definitions,
    generate_custom_field_values
)
from generators.tags import generate_tags, generate_task_tags

DB_PATH = Path("output/asana_simulation.sqlite")
SCHEMA_PATH = Path("schema.sql")

ORGANIZATION_ID = "org_001"
N_USERS = 7000


def execute_schema(conn):
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())


def insert_many(conn, table, rows):
    if not rows:
        return

    keys = rows[0].keys()
    columns = ", ".join(keys)
    placeholders = ", ".join(["?"] * len(keys))

    values = [tuple(row[k] for k in keys) for row in rows]

    conn.executemany(
        f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
        values
    )


def main():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    execute_schema(conn)

    # ---- Organization ----
    organization = [{
        "organization_id": ORGANIZATION_ID,
        "name": "Acme SaaS Inc",
        "domain": "acme.com",
        "created_at": "2022-01-01"
    }]
    insert_many(conn, "organizations", organization)

    # ---- Users ----
    users = generate_users(N_USERS)
    insert_many(conn, "users", users)

    # ---- Teams & Memberships ----
    teams = generate_teams(ORGANIZATION_ID)
    insert_many(conn, "teams", teams)

    memberships = generate_team_memberships(users, teams)
    insert_many(conn, "team_memberships", memberships)

    # ---- Projects & Sections ----
    projects = generate_projects(teams)
    insert_many(conn, "projects", projects)

    sections = generate_sections(projects)
    insert_many(conn, "sections", sections)

    # ---- Tasks & Subtasks ----
    tasks = generate_tasks(projects, sections, users)
    insert_many(conn, "tasks", tasks)

    subtasks = generate_subtasks(tasks)
    insert_many(conn, "tasks", subtasks)

    # ---- Comments ----
    comments = generate_comments(tasks, users)
    insert_many(conn, "comments", comments)

    # ---- Custom Fields ----
    field_defs = generate_custom_field_definitions(projects)
    insert_many(conn, "custom_field_definitions", field_defs)

    field_values = generate_custom_field_values(tasks, field_defs)
    insert_many(conn, "custom_field_values", field_values)

    # ---- Tags ----
    tags = generate_tags(ORGANIZATION_ID)
    insert_many(conn, "tags", tags)

    task_tags = generate_task_tags(tasks, tags)
    insert_many(conn, "task_tags", task_tags)

    conn.commit()
    conn.close()

    print("✅ Asana simulation database created at:", DB_PATH)


if __name__ == "__main__":
    main()
