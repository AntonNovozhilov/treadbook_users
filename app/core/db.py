import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_session,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings

load_dotenv(".env")

DATEBASE_URL = (
    f"postgresql+asyncpq:///"
    f"{settings.db_user}:{settings.db_password}@"
    f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

engine = create_async_engine(DATEBASE_URL, echo=False)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
)


async def get_async_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
