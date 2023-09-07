from fastapi import FastAPI
from enum import Enum

class Names(str, Enum):
    ivan = 'ivan'
    katya = 'katya'
    kostya = 'kostya'

app = FastAPI()

@app.get("/")
async def root():
    return {'Найдите секретный путь, который выдаст номер вашего билета'}

@app.get("/sum/{var1}/{var2}")
async def sum(var1: int, var2: int):
    return {"Ваш номер билета": var1+var2}

@app.get('/names/{name}')
async def get_name(name: Names):
    if name is Names.katya:
        return {'name': }