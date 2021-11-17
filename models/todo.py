from sqlalchemy import Column, Integer, String, engine

from db import Base

# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     content = Column(String)

Base.metadata.create_all(bind=engine)
