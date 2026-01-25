# Берём официальный образ Python (облегченная версия)
FROM python:3.11-slim

# Отключаем создание лишних файлов кеша и буферизацию вывода (чтобы логи видеть сразу)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую папку внутри "виртуального компьютера"
WORKDIR /app

# Сначала копируем только список библиотек (для кэширования)
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код внутрь
COPY . .
