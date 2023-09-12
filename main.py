from fastapi import FastAPI, Form
from enum import Enum
from pydantic import BaseModel


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
        return {'name': 'Katya'}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Konstantin"}]

@app.get('/query/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

class Para(BaseModel):
    name: str
    surname: str
    description: str
    gender: str

@app.post("/para/")
async def create_para(surname = Form(), name=Form(), description=Form(), gender=Form()):
    return {"surname": surname, "name": name, "description": description, "gender": gender}


