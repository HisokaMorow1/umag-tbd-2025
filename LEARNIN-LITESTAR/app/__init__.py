from litestar import Litestar, openapi
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin
from app.security import oauth2_auth
from app.config import settings
from app.db import db_config
from app.controllers import AuthController, TagController, TodoController, UserConstroller

slqa_plugin = SQLAlchemyPlugin(config = db_config)

openapi_config = openapi.OpenAPIConfig(
    title="TODO API",
    version="0.9.9",
    render_plugins=[SwaggerRenderPlugin(), ScalarRenderPlugin()],
)

app = Litestar(
    route_handlers=[TodoController,UserConstroller, TagController, AuthController],openapi_config=openapi_config, plugins = [slqa_plugin], 
    on_app_init = [oauth2_auth.on_app_init],
    debug = settings.debug,
)

