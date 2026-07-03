# Установка AI Studio

> Версия: v0.2.0-alpha

---

# Важно

AI Studio находится в стадии активной разработки.

На текущий момент инструкция предназначена в первую очередь для разработчиков, которые хотят ознакомиться с архитектурой проекта или принять участие в его развитии.

---

# Требования

Перед установкой необходимо установить:

- Python 3.12 или новее
- Git
- Ollama
- Git LFS (необязательно)
- Linux (рекомендуется Arch Linux, CachyOS или Ubuntu)

Windows пока официально не поддерживается.

---

# 1. Клонирование проекта

```bash
git clone <repository-url>

cd AI-Studio
```

---

# 2. Создание виртуального окружения

```bash
python -m venv .venv
```

Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

# 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# 4. Установка Ollama

Скачать Ollama можно с официального сайта.

После установки загрузить необходимую модель.

Например:

```bash
ollama pull qwen3
```

или

```bash
ollama pull llama3
```

---

# 5. Проверка Ollama

```bash
ollama list
```

Если модель отображается — всё готово.

---

# 6. Запуск AI Studio

Из корня проекта:

```bash
python main.py
```

---

# 7. Проверка системы

Проверить синтаксис:

```bash
python -m py_compile tools/*.py
python -m py_compile tests/tools/*.py
```

Проверить Filesystem Tool:

```bash
python -m tests.tools.test_filesystem
```

Проверить Terminal Tool:

```bash
python -m tests.tools.test_terminal
```

Все тесты должны завершиться без ошибок.

---

# Структура проекта

Основные директории:

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

# Возможные проблемы

## Python не найден

Убедитесь, что Python установлен и доступен в PATH.

---

## Ollama не запускается

Проверьте:

```bash
ollama serve
```

---

## Не находятся зависимости

Попробуйте обновить pip:

```bash
python -m pip install --upgrade pip
```

После чего снова установить зависимости.

---

# Следующие шаги

После успешной установки рекомендуется ознакомиться с:

- README.ru.md
- ROADMAP.md
- CONTRIBUTING.md

---

AI Studio активно развивается.

Начиная с версии v0.2.0-alpha проект получил полноценную систему инструментов и готов к дальнейшему развитию.
