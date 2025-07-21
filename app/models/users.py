from sqlalchemy import Column, String, UniqueConstraint, Boolean, Date
from app.models.base import BaseModel

from datetime import datetime


class User(BaseModel):
    """Пользователь."""

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    join_date = Column(Date, nullable=False, defoult=datetime.now)


    __table_args__ = (
        UniqueConstraint('username', name='uq_username'),
        UniqueConstraint('email', name='uq_email'),
    )