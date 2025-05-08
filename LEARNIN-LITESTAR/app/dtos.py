from litestar.plugins.sqlalchemy import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import TodoItem, User

class TodoItemReadDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"user"})

class TodoItemReadFullDTO(SQLAlchemyDTO[TodoItem]):
    pass

class TodoItemCreateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"id","user","user_id"})

class TodoItemUpdateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"id","user","user_id"}, partial=True)

class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"items"})

class UserReadFullDTO(SQLAlchemyDTO[User]):
    pass
