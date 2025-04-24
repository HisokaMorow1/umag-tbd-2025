from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import TodoItem

class TodoItemRepository(SQLAlchemySyncRepository[TodoItem]):
    model_type = TodoItem

def provide_todo_item_repo(db_session: Session) -> TodoItemRepository:
    return TodoItemRepository(session=db_session)