from pydantic import BaseModel

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
# class ItemCreate(ItemBase):
#     pass
#
# class Item(ItemBase):
#     id: int

class UserBase(BaseModel):
    surname: str

class UserCreate(UserBase):
    password: int

class User(UserBase):
    id: int

    class Config:
        orm_mode = True