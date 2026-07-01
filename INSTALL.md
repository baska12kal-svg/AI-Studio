# AI Studio Installation

This guide explains how to install AI Studio from scratch.

---

# Requirements

Install:

- Git
- Python 3.12+
- Ollama

---

# Clone Repository

SSH

```bash
git clone git@github.com:baska12kal-svg/AI-Studio.git
```

HTTPS

```bash
git clone https://github.com/baska12kal-svg/AI-Studio.git
```

Enter the project directory.

```bash
cd AI-Studio
```

---

# Create Virtual Environment

Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama from:

https://ollama.com

Verify installation.

```bash
ollama --version
```

---

# Download a Model

Example:

```bash
ollama pull qwen3:8b
```

or

```bash
ollama pull llama3.1:8b
```

---

# Configure AI Studio

Open:

```
config/config.yaml
```

Example:

```yaml
model: qwen3:8b
host: http://localhost:11434
temperature: 0.2
```

---

# Verify Installation

```bash
python -m tests.test_chat
```

Then:

```bash
python -m tests.test_project_query
```

If both commands complete successfully, AI Studio is ready to use.

---

# Troubleshooting

## Ollama is not running

```bash
ollama serve
```

---

## Model not found

```bash
ollama pull qwen3:8b
```

---

## Missing Python packages

```bash
pip install -r requirements.txt
```

---

# Documentation

- README.md
- ROADMAP.md
- CHANGELOG.md
- CONTRIBUTING.md
