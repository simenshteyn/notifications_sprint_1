from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from core import config
from models.template import Templates  # needed for SQLModel engine

db_name = config.POSTGRES_DB
db_host = config.POSTGRES_HOST
db_user = config.POSTGRES_USER
db_pass = config.POSTGRES_PASSWORD
db_port = config.POSTGRES_PORT
db_driver = "postgresql+asyncpg"

db_url = f"{db_driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine: Engine = create_async_engine(db_url, future=True)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
