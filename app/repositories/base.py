from typing import List, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T", bound="BaseRepositories")


class BaseRepositories:
    """Абстрактный класс для репозиториев."""

    def __init__(self, model):
        self.model = model

    async def get(self, pk: int, session: AsyncSession) -> T:
        """Получить объект по ID."""
        result = await session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return result.scalars().first()

    async def get_all(self, session: AsyncSession) -> List[T]:
        """Получить все объекты."""
        result = await session.execute(select(self.model))
        return result.scalars().all()

    async def create(self, data: dict, session: AsyncSession) -> T:
        """Создать объект."""
        obj = self.model(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def update(
        self, pk: int, data: dict, session: AsyncSession
    ) -> T:
        """Обновить объект."""
        obj = await self.get(pk, session)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, pk: int, session: AsyncSession) -> bool:
        """Удалить объект."""
        obj = await self.get(pk, session)
        if obj:
            await session.delete(obj)
            await session.commit()
