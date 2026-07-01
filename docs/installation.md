# Installation Guide

This guide explains how to install AI Studio on a clean system.

The project is designed to be simple to install, even for users with little experience using Git, Python or the terminal.

---

# Requirements

Before installing AI Studio, make sure the following software is available.

Required:

- Git
- Python 3.12 or newer
- Ollama

Recommended:

- Visual Studio Code
- Neovim
- Linux (Arch, Fedora or Ubuntu)

Windows is also planned to be fully supported.

---

# Clone the Repository

```bash
git clone https://github.com/<username>/AI-Studio.git

cd AI-Studio
```

---

# Create a Virtual Environment

Linux:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Windows:

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

Install Ollama from:

https://ollama.com

After installation verify:

```bash
ollama --version
```

---

# Download the Model

```bash
ollama pull qwen2.5-coder:7b
```

Verify:

```bash
ollama list
```

Expected output:

```text
qwen2.5-coder:7b
```

---

# Configure AI Studio

Open:

```text
config/config.yaml
```

Example:

```yaml
model: qwen2.5-coder:7b

host: http://127.0.0.1:11434

temperature: 0.2

timeout: 120

max_tokens: 4096

logging: true
```

---

# Run AI Studio

```bash
python main.py
```

Expected output:

```text
AI Studio

>>>
```

---

# Running Tests

Run all available tests:

```bash
python -m tests.test_llm

python -m tests.test_chat

python -m tests.test_project_index

python -m tests.test_project_query
```

If every test finishes successfully, the installation is complete.

---

# Troubleshooting

## Ollama does not respond

Check:

```bash
ollama ps
```

or

```bash
curl http://127.0.0.1:11434
```

---

## Model not found

Download it again:

```bash
ollama pull qwen2.5-coder:7b
```

---

## Python cannot import modules

Run the project from the repository root:

```bash
python -m tests.test_llm
```

instead of

```bash
python tests/test_llm.py
```

---

# Updating

Pull the latest version:

```bash
git pull
```

Update dependencies if necessary:

```bash
pip install -r requirements.txt
```

---

# Next Steps

After installation you can:

- explore the project architecture;
- read the development guide;
- contribute to the project;
- follow the roadmap.
