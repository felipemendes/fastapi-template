from pydantic import BaseModel

class SuccessfulOutput(BaseModel):
    message: str
    uuid: str

class ErrorOutput(BaseModel):
    message: str
