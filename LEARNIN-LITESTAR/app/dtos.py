from litestar.plugins.sqlalchemy import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import TodoItem

class TodoItemReadDTO(SQLAlchemyDTO[TodoItem]):
    pass

class TodoItemCreateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude=["id"])

class TodoItemUpdateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)