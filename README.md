# AI Studio

Local AI software engineering environment powered by Ollama.

AI Studio is an open-source project that aims to build a modular AI system for software development. Instead of being another chat interface, AI Studio is designed as a collection of independent components that understand projects, maintain context, plan work, generate code and interact with development tools.

Everything runs locally on your own machine.

> **Status:** Active Development • Core v0.1 Alpha

---

## Why AI Studio?

Most local AI applications focus on conversations.

AI Studio follows a different approach.

The language model is only one component of the system. Around it, AI Studio builds a modular architecture where every part has a dedicated responsibility.

Instead of asking a single model to do everything, AI Studio separates project analysis, planning, memory, code generation and tool execution into independent modules.

The long-term goal is to build a complete local software engineering environment rather than another AI chat application.

---

## Current Features

### Implemented

- Local LLM integration through Ollama
- Conversation management
- Session history
- Prompt system
- Project Analyzer
- Project Scanner (Python AST)
- Project Index
- Project Query API
- Project Brain

### In Development

- Tool Manager
- Memory Engine
- Orchestrator
- Planner
- Coder
- Reviewer
- Git integration
- Plugin system

---

## Architecture

```text
                          User
                            │
                            ▼
                     Conversation
                            │
                            ▼
                         Session
                            │
                            ▼
                            LLM
                            │
                            ▼
                         Ollama


                         Project
                  ┌────────┼────────┐
                  ▼        ▼        ▼
             Analyzer  Scanner   Brain
```

The architecture is intentionally modular. Every component has a single responsibility and can evolve independently without affecting the rest of the system.

---

## Goals

AI Studio is designed to become a complete local software engineering environment capable of:

- understanding existing projects;
- maintaining project knowledge;
- planning implementation;
- generating code;
- reviewing changes;
- interacting with Git repositories;
- executing development tools;
- operating completely offline.

---

## Roadmap

### Core

- [x] Configuration
- [x] Logger
- [x] Prompt Loader
- [x] Conversation
- [x] Session
- [x] Local LLM
- [x] Project Analyzer
- [x] Project Scanner
- [x] Project Query
- [x] Project Brain

### Next Milestones

- [ ] Tool Manager
- [ ] Memory Engine
- [ ] Orchestrator
- [ ] Planner
- [ ] Coder
- [ ] Reviewer
- [ ] Git Integration
- [ ] Plugin API

---

## Installation

Installation guides are currently being prepared.

The first public release will include complete step-by-step instructions for Linux and Windows, including guides written for users with little or no previous experience working with Python, Git or the terminal.

---

## Documentation

### User

- README.md — project overview
- INSTALL.md — installation guide (English)
- INSTALL_RU.md — инструкция по установке (Русский)

### Development

- ROADMAP.md
- CHANGELOG.md
- CONTRIBUTING.md
- ARCHITECTURE.md

---

## Contributing

Contributions, bug reports and ideas will be welcome after the first public alpha release.

---

## Project Status

Current milestone:

**Core v0.1 Alpha**

The core architecture is considered stable.

Development is now focused on tool integration, autonomous workflows and long-term memory.

---

## License

AI Studio will be released under the MIT License.
