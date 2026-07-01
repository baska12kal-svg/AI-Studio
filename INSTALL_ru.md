# Установка AI Studio

Это руководство поможет установить AI Studio с нуля.

Руководство написано для человека, который раньше не работал с проектом.

---

# Что понадобится

Перед началом убедитесь, что у вас установлены:

- Git
- Python 3.12 или новее
- Ollama

---

# Шаг 1. Клонирование проекта

Через SSH:

```bash
git clone git@github.com:baska12kal-svg/AI-Studio.git
```

или через HTTPS:

```bash
git clone https://github.com/baska12kal-svg/AI-Studio.git
```

Перейдите в папку проекта:

```bash
cd AI-Studio
```

---

# Шаг 2. Создание виртуального окружения

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

После активации в начале терминала должно появиться:

```text
(.venv)
```

---

# Шаг 3. Установка зависимостей

Выполните:

```bash
pip install -r requirements.txt
```

Дождитесь окончания установки.

---

# Шаг 4. Установка Ollama

Скачайте Ollama с официального сайта.

После установки проверьте:

```bash
ollama --version
```

Если версия отображается — всё установлено правильно.

---

# Шаг 5. Загрузка модели

Например:

```bash
ollama pull qwen3:8b
```

или

```bash
ollama pull llama3.1:8b
```

---

# Шаг 6. Проверка конфигурации

Откройте файл:

```
config/config.yaml
```

Убедитесь, что указана установленная модель.

Пример:

```yaml
model: qwen3:8b
host: http://localhost:11434
temperature: 0.2
```

---

# Шаг 7. Проверка работы

Запустите:

```bash
python -m tests.test_chat
```

Если всё установлено правильно, AI Studio ответит на тестовое сообщение.

---

# Проверка анализа проекта

Запустите:

```bash
python -m tests.test_project_query
```

Если выводится информация о проекте — анализатор работает.

---

# Возможные проблемы

## Ollama не отвечает

Запустите:

```bash
ollama serve
```

---

## Модель не найдена

Загрузите модель ещё раз:

```bash
ollama pull qwen3:8b
```

---

## Не найдены библиотеки Python

Повторите установку:

```bash
pip install -r requirements.txt
```

---

# Готово

Если все проверки прошли успешно, AI Studio готов к работе.

Следующим шагом рекомендуется прочитать README.md, чтобы познакомиться с архитектурой проекта.
