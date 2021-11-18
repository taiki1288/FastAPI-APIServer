from fastapi import FastAPI

from db import SessionLocal, engine, Base
from routers import todo
# modelsディレクトリのtodo.pyをインポートしてTodoモデルを読み込み
from models.todo import Todo

# テーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)