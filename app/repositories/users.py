from app.models.users import User
from app.repositories.base import BaseRepositories


class UserCRUD(BaseRepositories):
    """CRUD пользователей."""


user = UserCRUD(User)
