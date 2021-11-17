from typing import Optional
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    content: Optional[str] = None

class TodoCreate(TodoBase):
    # titleとcontentが格納されているTodoBaseを引数に
    pass

class TodoCreateResponse(TodoCreate):
    id: int

class Todo(BaseModel):
    id: int
    content: Optional[str] = None

    class Config:
        orm_mode = True