from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy import delete
from sqlalchemy.orm.exc import NoResultFound
from database.connection import async_session

from models.user import User
from schemas.user import UserCreateInput

class UserService:
    async def create(name: str, email: str):
        async with async_session() as session:
            new_user = User(name=name, email=email)
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def read(user_id: UUID):
        async with async_session() as session:
            try:
                result = await session.execute(select(User).where(User.id == user_id))
                return result.scalar()
            except NoResultFound:
                return None

    async def update(user_id: UUID, user: UserCreateInput):
        async with async_session() as session:
            existing_user = await session.get(User, user_id)

            if existing_user:
                existing_user.name = user.name
                existing_user.email = user.email
                await session.commit()
                await session.refresh(existing_user)
                return existing_user
            else:
                return None

    async def delete(user_id: UUID):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id == user_id))
            await session.commit()
