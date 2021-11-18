from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoCreate

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todos(db: Session):
    return db.query(Todo).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    db.delete(todo)
    db.commit()