from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas.user import User
from viajei_api.schemas.user_public import UserPublic

app = FastAPI()


@app.post('/auth/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def login(user: User): ...
