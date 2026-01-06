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
-- Team Memberships
-- Projects
-- Sections
-- Tasks
-- Comments
-- Custom Field Definitions
-- Custom Field Values
-- Tags
-- Task-Tag Associations
