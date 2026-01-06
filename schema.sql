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
