from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserSchema(BaseModel):
    """Пользователь."""

    username: str = Field(..., min_length=3, max_length=20, description="Ник")
    email: EmailStr = Field(..., description="Email")

    @field_validator("email")
    @classmethod
    def validator_len_email(cls, value: str) -> str:
        """Проверка длины email."""
        if len(value) < 6 or len(value) > 50:
            raise ValueError("Email должен быть от 6 до 50 символов")
        return value


class UserRead(UserSchema):
    """Пользователь для чтения."""

    id: int = Field(..., description="ID пользователя")
    is_superuser: bool = Field(False, description="Суперпользователь")
    is_active: bool = Field(True, description="Активный")
    join_date: datetime = Field(
        default_factory=datetime.now, description="Дата регистрации"
    )

    class Config:
        orm_mode = True


class UserCreate(UserSchema):
    """Пользователь для создания."""

    password: str = Field(
        ..., min_length=6, max_length=128, description="Пароль"
    )


class UserUpdate(UserSchema):
    """Обновление пользователя."""

    username: Optional[str] = Field(
        min_length=3, max_length=20, description="Ник"
    )
    email: Optional[EmailStr] = Field(description="Email")
    password: Optional[str] = Field(
        min_length=6, max_length=128, description="Пароль"
    )
