from fastapi import APIRouter, HTTPException

from helpers.utils import validate_uuid

from schemas.user import UserCreateInput, UserListOutput
from schemas.outputs import SuccessfulOutput, ErrorOutput

from services.user_service import UserService

user_router = APIRouter(prefix='/user')

@user_router.post('/create', response_model=SuccessfulOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        new_user = await UserService.create(name=user_input.name, email=user_input.email)
        return SuccessfulOutput(message="OK", uuid=f'{new_user.id}')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.get('/{user_id}', response_model=UserListOutput, responses={400: {'model': ErrorOutput}})
async def user_read(user_id: str):
    user_uuid = validate_uuid(user_id)

    try:
        user = await UserService.read(user_id=user_uuid)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@user_router.put('/update/{user_id}', response_model=UserListOutput, responses={400: {'model': ErrorOutput}})
async def user_update(user_id: str, user_input: UserCreateInput):
    user_uuid = validate_uuid(user_id)

    try:
        updated_user = await UserService.update(user_id=user_uuid, user=user_input)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@user_router.delete('/delete/{user_id}', response_model=SuccessfulOutput, responses={400: {'model': ErrorOutput}})
async def user_delete(user_id: str):
    user_uuid = validate_uuid(user_id)

    try:
        await UserService.delete(user_id=user_uuid)
        return SuccessfulOutput(message='OK', uuid=f'{user_uuid}') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
