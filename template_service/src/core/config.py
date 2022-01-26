import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "fitter")

REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "change_this2")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "templates")

SERVICE_PROTOCOL = os.getenv("SERVICE_PROTOCOL", "http")
SERVICE_HOST = os.getenv("SERVICE_HOST")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 8000))
SERVICE_API_VERSION = int(os.getenv("SERVICE_API_VERSION", 1))

NGINX_PORT = int(os.getenv("NGINX_PORT", 80))
