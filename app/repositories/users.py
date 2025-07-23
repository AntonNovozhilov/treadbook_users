from app.models.users import User
from app.repositories.base import BaseRepositories
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserCRUD(BaseRepositories):
    """CRUD пользователей."""

    async def get_by_email(self, email: str, session: AsyncSession):
        result = await session.execute(select(User).where(User.email == email))
        result = result.scalars().first()
        return result


user = UserCRUD(User)
