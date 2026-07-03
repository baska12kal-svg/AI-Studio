# Contributing to AI Studio

Thank you for your interest in AI Studio.

Although the project is currently in the Alpha stage, contributions, bug reports and ideas are welcome.

---

# Development Philosophy

AI Studio is developed incrementally.

Every release introduces one complete subsystem before moving to the next milestone.

Large architectural changes are preferred over isolated feature additions.

---

# Code Style

General principles:

- Write readable code.
- Prefer simplicity over cleverness.
- Keep modules independent.
- Every class should have a single responsibility.
- Avoid unnecessary dependencies.

---

# Tool Development

Every new Tool must:

- inherit from `Tool`;
- return `ToolResult`;
- be registered in `ToolManager`;
- include automated tests;
- follow the existing project architecture.

Current Tool API:

```python
class Tool:

    @property
    def name(self):
        ...

    def execute(self, action: str, **kwargs):
        ...
```

---

# Testing

Before every commit, verify that the project builds successfully.

Compile:

```bash
python -m py_compile tools/*.py
python -m py_compile tests/tools/*.py
```

Run Filesystem Tool tests:

```bash
python -m tests.tools.test_filesystem
```

Run Terminal Tool tests:

```bash
python -m tests.tools.test_terminal
```

No release should be published while any test is failing.

---

# Commit Style

Recommended commit prefixes:

```text
feat:
fix:
refactor:
docs:
test:
release:
```

Examples:

```text
feat(tools): implement FilesystemTool

feat(tools): implement TerminalTool

docs: update README

release: AI Studio v0.2.0-alpha
```

---

# Pull Requests

Before opening a Pull Request:

- ensure the project builds successfully;
- run all available tests;
- update documentation if necessary;
- keep commits focused on a single feature.

---

# Reporting Issues

When reporting bugs, include:

- operating system;
- Python version;
- AI Studio version;
- reproduction steps;
- expected behavior;
- actual behavior;
- logs if available.

---

# Project Principles

The project follows several long-term principles:

- Local First
- Modular Architecture
- Clear Interfaces
- Automated Testing
- Incremental Development
- Transparent AI

These principles should guide every contribution to AI Studio.
