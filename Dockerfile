# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт (если потребуется)
EXPOSE 8000

# Команда по умолчанию при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
