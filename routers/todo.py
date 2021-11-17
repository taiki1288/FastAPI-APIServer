from typing import List
from fastapi import APIRouter

import schemas.todo as todo_schema
# schema.todoをtodo_schemaと読み替えてからimportする。

router = APIRouter()

# 全てのTodoを取得
@router.get("/todos", response_model=List[todo_schema.Todo])
# response_modelを使ってレスポンスモデルを定義(scemaのTodoクラスを取ってきている)
# 全てのTodoを取得したいからListを使って取得。
async def todo_lists():
    return [todo_schema.Todo(id=1, title="first todo")]

# 一つのTodoを取得
@router.get("/todos/{todo_id}")
async def get_todo():
    pass

# Todoの登録
@router.post("/todos", response_model=todo_schema.TodoCreateResponse)
# responsemodel=todo_schema.TodoCreateResponseでTodoCreateResponseのidを渡している。
async def create_todo(todo_body: todo_schema.TodoCreate):
    return todo_schema.TodoCreateResponse(id=1, **todo_body.dict())
    # リクエストボディにidを付与してレスポンスデータを返している。todo_schema.TodoCreateをdict型に変換している。
    # **でtodo_schema.TodoCreateResponsのkeyとvalueとid1を持つインスタンスを生成している。

# Todoの更新
@router.put("/todos/{todo_id}", response_model=todo_schema.TodoCreateResponse)
async def update_todo(todo_id: int, todo_body: todo_schema.TodoCreate):
    return todo_schema.TodoCreateResponse(id=todo_id, **todo_body.dict())

# Todoを削除
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    return

