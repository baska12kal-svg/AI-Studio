# Installing AI Studio

> Version: v0.2.0-alpha

---

# Notice

AI Studio is currently in active development.

This guide is intended for developers and contributors who want to explore the project or participate in its development.

---

# Requirements

Before installing AI Studio, make sure the following software is available:

- Python 3.12 or newer
- Git
- Ollama

---

# 1. Clone the Repository

```bash
git clone <repository-url>

cd AI-Studio
```

---

# 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Install Ollama

Download Ollama from the official website.

After installation, download a language model.

Example:

```bash
ollama pull qwen3
```

or

```bash
ollama pull llama3
```

---

# 5. Verify Ollama

```bash
ollama list
```

If the model appears in the list, Ollama is ready.

---

# 6. Run AI Studio

From the project root:

```bash
python main.py
```

---

# 7. Verify the Installation

Compile all tools:

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

All commands should finish without errors.

---

# Project Structure

Main directories:

```text
agents/
config/
core/
docs/
memory/
projects/
prompts/
tests/
tools/
web/
```

---

# Troubleshooting

## Python is not found

Make sure Python is installed and available in your PATH.

---

## Ollama does not start

Try running:

```bash
ollama serve
```

---

## Dependency installation fails

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then install the requirements again.

---

# Next Steps

After installation, it is recommended to read:

- README.md
- ROADMAP.md
- CONTRIBUTING.md

---

AI Studio is under active development.

Starting with **v0.2.0-alpha**, the project includes a unified Tool System that provides the foundation for future autonomous development features.
