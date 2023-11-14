from typing import List
from pydantic import BaseModel, UUID4

class UserCreateInput(BaseModel):
    """
    Represents the input model for creating a user.
    """
    name: str
    email: str

class UserListOutput(BaseModel):
    """
    Represents the output model for listing user details.
    """
    id: UUID4
    name: str
    email: str

    class Config:
        from_attributes = True
