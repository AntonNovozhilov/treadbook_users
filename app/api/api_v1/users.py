from fastapi import APIRouter, Depends
from app.schemas import users
from app.repositories.users import user
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from fastapi.exceptions import HTTPException
from http import HTTPStatus
from app.core.security import get_password_hash

router = APIRouter()

@router.get('/', response_model=list[users.UserRead])
async def get_users(session: AsyncSession = Depends(get_async_session)) -> list[users.UserRead]:
    return await user.get_all(session)

@router.get('/{pk}', response_model=users.UserRead)
async def get_user(pk: int, session: AsyncSession = Depends(get_async_session)) -> users.UserRead:
    return await user.get(pk, session)

@router.post('/', response_model=users.UserRead)
async def create_user(data: users.UserCreate, session: AsyncSession = Depends(get_async_session)) -> users.UserRead:
    existing_user = await user.get_by_email(data.email, session)
    if existing_user:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Пользователь с таким email уже зарегистрирован.')
    password_hash = get_password_hash(data.password)
    data.password = password_hash
    data_obj = data.model_dump()
    return await user.create(data_obj, session)

@router.patch('/{pk}', response_model=users.UserRead)
async def update_user(pk: int, data: users.UserUpdate, session: AsyncSession = Depends(get_async_session)) -> users.UserRead:
    return await user.update(pk, data, session)

    
@router.delete('/{pk}', response_model=users.UserRead)
async def delete_user(pk: int, session: AsyncSession = Depends(get_async_session)) -> users.UserRead:
    result = await user.delete(pk, session)
    return result