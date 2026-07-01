# AI Studio Architecture

## Overview

AI Studio is designed as a modular local AI software engineering environment.

Instead of relying on a single prompt, the system is divided into independent components with clearly defined responsibilities.

Every module should solve one problem and communicate with other modules through well-defined interfaces.

---

# High-Level Architecture

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

                             │

                             ▼

                     Project System

           ┌──────────┼──────────┐
           ▼          ▼          ▼
      Analyzer    Scanner     Brain
```

---

# Core

The `core` package contains the fundamental building blocks of AI Studio.

Current modules include:

- configuration
- logger
- prompt loader
- conversation
- session
- LLM interface
- project system

The core should remain small, stable and independent.

---

# Conversation

Responsible for maintaining message history.

Responsibilities:

- store messages
- append new messages
- provide conversation context

---

# Session

A lightweight wrapper around Conversation.

Responsibilities:

- initialize conversations
- load the system prompt
- prepare messages for the language model

---

# LLM

Provides a unified interface for communicating with Ollama.

Responsibilities:

- load configuration
- send requests
- receive responses
- isolate Ollama-specific code

---

# Project System

The Project System provides AI Studio with knowledge about source code.

Current modules:

Analyzer

- indexes project files

Scanner

- parses Python files
- extracts classes
- extracts functions
- extracts imports

Brain

- summarizes project structure

Query

- provides search APIs

---

# Future Architecture

The following modules are planned.

```text
                    Tool Manager

                          │

      ┌──────────────┼──────────────┐
      ▼              ▼              ▼

   Filesystem      Python         Git

                          │

                          ▼

                     Memory Engine

                          │

                          ▼

                     Orchestrator

          ┌────────┼─────────┬─────────┐
          ▼        ▼         ▼         ▼

      Planner   Coder   Reviewer   Researcher
```

---

# Design Principles

AI Studio follows several architectural principles.

## Single Responsibility

Each module should have one primary responsibility.

---

## Modularity

Components should communicate through clear interfaces.

Avoid tightly coupled implementations.

---

## Local First

Everything should work without cloud services whenever possible.

---

## Extensibility

New modules should integrate without requiring changes to existing components.

---

## Testability

Every major module should have dedicated tests.

---

# Current Status

Core architecture is considered stable.

Future development will focus on expanding capabilities without breaking the existing architecture.
