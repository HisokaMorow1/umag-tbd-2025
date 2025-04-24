from typing import Sequence
from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import ComparisonFilter
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.dtos import TodoItemCreateDTO, TodoItemReadDTO, TodoItemUpdateDTO
from app.models import TodoItem
from app.repositories import TodoItemRepository, provide_todo_item_repo

class TodoController(Controller):
    path = "/items"
    return_dto = TodoItemReadDTO
    dependencies = {
        "todoitem_repo": Provide(provide_todo_item_repo)
    }

    @get("/")
    async def get_list(self, todoitem_repo: TodoItemRepository, done: bool | None = None) -> Sequence[TodoItem]:
        if done is None:
            return todoitem_repo.list()
        return todoitem_repo.list(ComparisonFilter("done","eq",done)) 

    @post("/",dto=TodoItemCreateDTO)
    async def add_todo(self, data: TodoItem, db_session:Session) -> Sequence[TodoItem]:
        with db_session.begin():
            db_session.add(data)
        return db_session.execute(select(TodoItem)).scalars().all()
    
    @get("/{item_id:int}")
    async def get_item(self, item_id: int, todoitem_repo: TodoItemRepository) -> TodoItem:
        try:
            return todoitem_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")
    
    @patch("/{item_id:int}", dto=TodoItemUpdateDTO)
    async def update_item(self, item_id: int, data: DTOData[TodoItem], db_session: Session) -> TodoItem:
        data_dict = data.as_builtins()
        item =  db_session.execute(select(TodoItem).where(TodoItem.id == item_id)).scalar_one()
        for field in ("title", "done"):
            if data_dict[field] is not None:
                setattr(item, field, data_dict[field])
        db_session.commit()
        return item
    
    @delete("/{item_id:int}")
    async def delete_item(self, item_id: int, todoitem_repo: TodoItemRepository) -> None:
        todoitem_repo.delete(item_id)



    # @put("/{item_id:int}")
    # async def update_item(item_id: int ,data: TodoItem) -> list[TodoItem]:
    #     for t in TODO_LIST:
    #         if t.id == item_id:
    #             t.title = data.title
    #             t.done = data.done
    #             break
    #     return TODO_LIST


    # @patch("/{item_id:int}")
    # async def patch_item(item_id: int ,data: TodoItemUpdate) -> list[TodoItem]:
    #     for t in TODO_LIST:
    #         if t.id == item_id:
    #             if data.title is not None:
    #                 t.title = data.title
    #             if data.done is not None:
    #                 t.done = data.done
    #             break
    #     return TODO_LIST

    # @delete("/{item_id:int}")
    # async def delete_item(item_id:int) -> None:
    #     for t in TODO_LIST:
    #         if t.id == item_id:
    #             TODO_LIST.remove(t)
