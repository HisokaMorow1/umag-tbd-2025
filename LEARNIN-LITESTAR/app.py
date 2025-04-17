from dataclasses import dataclass
from typing import Sequence
from litestar import Controller, Litestar, delete, get, patch, post, put
from litestar.exceptions import HTTPException
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin, SQLAlchemySyncConfig
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

class Base(DeclarativeBase):
    pass

class TodoItem(Base):
    __tablename__ = "todo_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    done: Mapped[bool]



# @dataclass
# class TodoItem:
#     id: int
#     title: str
#     done: bool

# @dataclass
# class TodoItemUpdate:
#     title: str | None = None
#     done: bool | None = None



# TODO_LIST: list[TodoItem] = [
#     TodoItem(id = 1, title= "Aprender python", done = True),
#     TodoItem(id = 2,title= "Aprender SQLAlchemy", done = True),
#     TodoItem(id = 3,title= "Aprender Litestar", done = False),
# ]

class TodoController(Controller):
    path = "/items"
    @get("/")
    async def get_list(self, db_session: Session, done: bool | None = None) -> Sequence[TodoItem]:
        stmt = select(TodoItem)
        if done is not None:
            stmt = stmt.filter(TodoItem.done == done)
        return db_session.execute(stmt).scalars().all()

    @post("/")
    async def add_todo(self, data: TodoItem, db_session:Session) -> Sequence[TodoItem]:
        with db_session.begin():
            db_session.add(data)
        return db_session.execute(select(TodoItem)).scalars().all()
    
    @get("/{item_id:int}")
    async def get_item(self, item_id: int, db_session: Session) -> TodoItem:
        try:
            return db_session.execute(select(TodoItem).where(TodoItem.id == item_id)).scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")

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

@get("/") 
async def hello_world() -> str:
    return "Hello, world!"

db_config = SQLAlchemySyncConfig(
    connection_string="sqlite:///db.sqlite3",create_all=True, metadata=Base.metadata
)

slqa_plugin = SQLAlchemyPlugin(config = db_config)

app = Litestar(
    route_handlers=[hello_world, TodoController],plugins = [slqa_plugin],debug=True
)

