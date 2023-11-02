# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости из pyproject.toml
RUN pip install --no-cache-dir poetry && poetry install

# Команда для запуска вашего проекта
CMD ["poetry", "run", "python", "personal_assistant_folder/personal_assistant.py"]
