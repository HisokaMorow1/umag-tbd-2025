from advanced_alchemy.filters import CollectionFilter
from advanced_alchemy.repository import SQLAlchemySyncRepository
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.models import Tag, TodoItem,User

password_hasher = PasswordHash.recommended()

class TodoItemRepository(SQLAlchemySyncRepository[TodoItem]):
    model_type = TodoItem
    def add_with_tags(self, todo_item: TodoItem,tags_repo: "TagRepository",**kwargs)-> TodoItem:
        todo_item.tags = tags_repo.list(CollectionFilter("id", [t.id for t in todo_item.tags]))
        return self.add(todo_item, **kwargs)


async def provide_todo_item_repo(db_session: Session) -> TodoItemRepository:
    return TodoItemRepository(session=db_session)

class UserRepository(SQLAlchemySyncRepository[User]):
    model_type = User

    def add_witch_password_hash(self, user: User, **kwargs)->User:
        user.password = password_hasher.hash(user.password)
        return self.add(user, **kwargs)
    
    def check_password(self, username: str, password: str) -> bool:
        user = self.get(username, id_attribute ="username")

        return password_hasher.verify(password, user.password)

async def provide_user_repo(db_session: Session) -> TodoItemRepository:
    return UserRepository(session=db_session)

class TagRepository(SQLAlchemySyncRepository[Tag]):
    model_type = Tag

async def provide_tag_repo(db_session: Session) -> TagRepository:
    return TagRepository(session=db_session)