from db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String) 
    phone = Column(String)
    isprime= Column(Boolean)