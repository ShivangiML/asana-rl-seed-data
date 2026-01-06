-- Asana RL Environment Schema
-- Simulated B2B SaaS company (~7000 employees)

-- Organizations / Workspaces 
CREATE TABLE organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT,
    created_at TIMESTAMP NOT NULL
);

-- Users
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    job_title TEXT,
    department TEXT,
    role TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    deactivated_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- Teams
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- Team Memberships
CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    role TEXT,
    joined_at TIMESTAMP NOT NULL,
    left_at TIMESTAMP,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Projects
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    project_type TEXT,
    created_at TIMESTAMP NOT NULL,
    archived_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Sections
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Tasks
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    parent_task_id TEXT,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL,
    due_date DATE,
    completed BOOLEAN NOT NULL DEFAULT 0,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- Comments
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Custom Field Definitions
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Custom Field Values
CREATE TABLE custom_field_values (
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT,
    PRIMARY KEY (task_id, field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

-- Tags
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- Task-Tag Associations
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
