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
    created_at TIMESTAMP NOT NULL,
    deactivated_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- Teams
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
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
-- Comments
-- Custom Field Definitions
-- Custom Field Values
-- Tags
-- Task-Tag Associations
