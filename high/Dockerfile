FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean
    

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
COPY . /code