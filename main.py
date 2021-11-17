from fastapi import FastAPI

from db import SessionLocal, engine, Base
from routers import todo
# modelsディレクトリのtodo.pyをインポートしてTodoモデルを読み込み
from models.todo import Todo

# テーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

# get_db()関数を使用してDBへのアクセスを行う。
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(todo.router)