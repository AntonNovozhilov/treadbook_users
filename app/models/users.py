from datetime import datetime

from sqlalchemy import Boolean, Column, Date, String, UniqueConstraint

from app.models.base import BaseModel


class User(BaseModel):
    """Пользователь."""

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    join_date = Column(Date, nullable=False, default=datetime.now)

    __table_args__ = (
        UniqueConstraint("username", name="uq_username"),
        UniqueConstraint("email", name="uq_email"),
    )
