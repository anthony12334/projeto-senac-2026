from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas import Message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def ola_mundo():
    return{"message":"olá! mundo"}


    