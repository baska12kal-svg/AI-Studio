# Development Guide

This document describes the development principles and workflow used in AI Studio.

---

# Philosophy

AI Studio is built with a strong focus on simplicity, modularity and maintainability.

The project should remain easy to understand, easy to extend and easy to test.

Whenever possible:

- prefer simple solutions;
- avoid unnecessary abstractions;
- keep modules independent;
- keep responsibilities clear.

---

# Project Structure

```
AI-Studio/

├── agents/
├── config/
├── core/
├── docs/
├── logs/
├── memory/
├── prompts/
├── scripts/
├── tests/
├── tools/
├── web/

├── main.py
├── requirements.txt
├── README.md
├── ROADMAP.md
└── CHANGELOG.md
```

---

# Core Principles

## Single Responsibility

Every module should solve one problem.

Bad:

```
llm.py

- loads config
- manages memory
- edits files
- executes git
```

Good:

```
llm.py

- communicates with Ollama
```

---

## Modular Design

Every subsystem should be replaceable without affecting unrelated parts of the project.

For example:

Conversation should not know how Project Analyzer works.

Project Analyzer should not know how Memory works.

---

## Local First

Everything should work locally whenever possible.

Cloud services should remain optional.

---

## Type Safety

Prefer dataclasses and type hints.

Avoid passing anonymous dictionaries through the project when a dedicated type makes the code clearer.

Example:

```python
ProjectFile(...)
```

instead of

```python
{
    "name": "...",
    "path": "...",
}
```

---

## Testing

Every important module should have its own test.

Examples:

```
tests/

test_llm.py

test_chat.py

test_project_index.py

test_project_query.py
```

Changes that break existing tests should be fixed before merging.

---

# Coding Style

General rules:

- Python 3
- PEP 8
- meaningful variable names
- small functions
- small classes
- explicit interfaces
- avoid global state

---

# Git Workflow

Typical development cycle:

```bash
git checkout main

git pull

# implement changes

git add .

git commit -m "Describe the change"
```

Create logical commits.

Avoid mixing unrelated changes into one commit.

---

# Documentation

Documentation should evolve together with the code.

Whenever a feature is added:

- update README if necessary;
- update ROADMAP if plans change;
- update CHANGELOG;
- add documentation when appropriate.

---

# Roadmap

Development follows the roadmap described in:

```
ROADMAP.md
```

Current priorities:

1. Tool Manager
2. Memory Engine
3. Orchestrator
4. Planner
5. Coder
6. Reviewer

---

# Contributing

Before implementing large features:

- discuss the idea;
- verify that it matches the project architecture;
- avoid introducing unnecessary complexity.

The goal is long-term maintainability rather than short-term feature growth.
