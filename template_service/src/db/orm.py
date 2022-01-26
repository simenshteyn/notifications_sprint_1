from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine

from core import config
from models.template import Templates  # needed for SQLModel engine

db_name = config.POSTGRES_DB
db_host = config.POSTGRES_HOST
db_user = config.POSTGRES_USER
db_pass = config.POSTGRES_PASSWORD
db_port = config.POSTGRES_PORT
db_driver = "postgresql"

db_url = f"{db_driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine: Engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


async def get_engine() -> Engine:
    return engine
