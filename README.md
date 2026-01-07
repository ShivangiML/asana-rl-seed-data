# Asana RL Seed Data Simulation

This repository contains a complete pipeline for generating a realistic, enterprise-scale Asana workspace dataset. The dataset is designed to serve as high-quality seed data for reinforcement learning (RL) environments that evaluate computer-use AI agents on project management workflows. The simulation models a B2B SaaS company with approximately 7,000 users across engineering, product, marketing, and operations teams.

---

## 🎯 Project Objectives

- Create a realistic Asana-like relational schema
- Generate enterprise-grade synthetic data with no trivial shortcuts
- Maintain temporal, relational, and logical consistency
- Support RL evaluation for task management and workflow automation agents

---

## 🧱 Modeled Entities

- Organizations
- Users (with roles)
- Teams and team memberships
- Projects and sections
- Tasks and subtasks
- Comments
- Custom fields and values
- Tags and task-tag associations

---

## 🗂 Repository Structure

- schema.sql — database schema
- src/ — data generation pipeline
- output/ — generated SQLite database

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
rm output/asana_simulation.sqlite
python src/main.py
