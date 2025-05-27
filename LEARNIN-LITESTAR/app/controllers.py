from typing import Annotated, Any, Sequence
from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import ComparisonFilter
from litestar import Controller, Request, get, post, patch, delete, Response
from litestar.contrib.jwt import OAuth2Login, Token
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.enums import RequestEncodingType
from litestar.exceptions import HTTPException
from litestar.params import Body
from app.dtos import TagReadDTO, TodoItemCreateDTO, TodoItemReadDTO, TodoItemUpdateDTO, UserCreateDTO, UserLoginDTO, UserReadDTO, UserReadFullDTO, TodoItemReadFullDTO
from app.models import Tag, TodoItem, User
from app.repositories import TagRepository, TodoItemRepository, UserRepository, provide_tag_repo, provide_todo_item_repo, provide_user_repo
from .security import oauth2_auth

class TodoController(Controller):
    path = "/items"
    tags = ["items"]
    return_dto = TodoItemReadDTO
    dependencies = {
        "todoitem_repo": Provide(provide_todo_item_repo)
    }

    @get("/{item_id:int}/list", return_dto=TodoItemReadFullDTO)
    async def list_item_full(self, todoitem_repo: TodoItemRepository, item_id: int) -> TodoItem:
        try:
            return todoitem_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")


    @get("/")
    async def get_list(self, todoitem_repo: TodoItemRepository, done: bool | None = None) -> Sequence[TodoItem]:
        if done is None:
            return todoitem_repo.list()
        return todoitem_repo.list(ComparisonFilter("done","eq",done)) 

    @post("/",dto=TodoItemCreateDTO, dependencies = {"tags_repo": Provide(provide_tag_repo)} )
    async def add_todo(self, todoitem_repo:TodoItemRepository, tags_repo: TagRepository, data: TodoItem) -> TodoItem:
        return todoitem_repo.add_with_tags(data,tags_repo, auto_commit=True)
    
    @get("/{item_id:int}")
    async def get_item(self, item_id: int, todoitem_repo: TodoItemRepository) -> TodoItem:
        try:
            return todoitem_repo.get(item_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"Item con id ={item_id} no existe")
    
    @patch("/{item_id:int}", dto=TodoItemUpdateDTO)
    async def update_item(self, todoitem_repo: TodoItemRepository, item_id: int, data: DTOData[TodoItem]) -> TodoItem:
        item, _ = todoitem_repo.get_and_update(match_fields= "id", id=item_id, **data.as_builtins(),auto_commit=True)
        return item
    
    @delete("/{item_id:int}")
    async def delete_item(self, item_id: int, todoitem_repo: TodoItemRepository) -> None:
        todoitem_repo.delete(item_id,auto_commit=True)



class UserConstroller(Controller):
    path = "/users"
    tags = ["users"]
    dependencies = {
        "users_repo": Provide(provide_user_repo)
    }
    return_dto = UserReadDTO

    @get("/")
    async def list_users(self, users_repo: UserRepository) -> Sequence[User]:
        return users_repo.list()
    
    @get("/me")
    async def get_my_user(self, request: "Request[User,Token,Any]") -> User:
        return request.user

    @get("/{user_id:int}")
    async def get_user(self, users_repo: UserRepository, user_id: int) -> User:
        try:
            return users_repo.get(user_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"User con id ={user_id} no existe")
        
    @get("/{user_id:int}/full", return_dto=UserReadFullDTO)
    async def get_user_full(self, users_repo: UserRepository, user_id: int) -> User:
        try:
            return users_repo.get(user_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail=f"User con id ={user_id} no existe")
        
    @post("/", dto=UserCreateDTO)
    async def add_user(self, users_repo: UserRepository, data: User) -> User:
        return users_repo.add_witch_password_hash(data, auto_commit=True)

class TagController(Controller):
    path = "/tags"
    tags = ["tags"]
    return_dto = TagReadDTO
    dependencies = {
        "tag_repo": Provide(provide_tag_repo)
    }
    @get("/")
    async def list_tags(self, tag_repo: TagRepository) -> Sequence[Tag]:
        return tag_repo.list()
    
class AuthController(Controller):
    path = "/auth"
    tags = ["auth"]

    @post("/login", dto=UserLoginDTO, dependencies = {"users_repo": Provide(provide_user_repo)})
    async def login(self, data: Annotated[User, Body(media_type = RequestEncodingType.URL_ENCODED)], users_repo: UserRepository) -> Response[OAuth2Login]:
        user = users_repo.get_one_or_none(username = data.username)
        
        #raise Exception("Algo Salio Mal")
    
        if user is None or not users_repo.check_password(data.username, data.password):
            raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
        
        return oauth2_auth.login(identifier = user.username)
        
