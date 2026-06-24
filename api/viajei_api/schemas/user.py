from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str


class UserDB(User):
    id = int
