from litestar.plugins.sqlalchemy import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Tag, TodoItem, User

class TodoItemReadDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"user"})

class TodoItemReadFullDTO(SQLAlchemyDTO[TodoItem]):
    pass

class TodoItemCreateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"id","user","tags.0.name"})

class TodoItemUpdateDTO(SQLAlchemyDTO[TodoItem]):
    config = SQLAlchemyDTOConfig(exclude={"id","user","user_id"}, partial=True)

class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"items"})

class UserReadFullDTO(SQLAlchemyDTO[User]):
    pass

class TagReadDTO(SQLAlchemyDTO[Tag]):
    pass

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id","items"})