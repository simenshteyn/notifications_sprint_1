FROM python:3.9.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY ./src /app/rabbit_consumer
WORKDIR /app/rabbit_consumer

CMD ["python", "app.py"]