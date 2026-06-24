from pydantic import BaseModel


class UserPublic(BaseModel):
    email: str
