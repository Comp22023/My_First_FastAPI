from sqlalchemy import create_engine, Column, Integer, String
from database import Base
import sqlalchemy

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String)
    pasword = Column(String)
    surname = Column(String)
    name = Column(String)
    father_name = Column(String)
    age = Column(Integer, default = 18)
    growth = Column(Integer) #Рост
    weight = Column(Integer) #Вес