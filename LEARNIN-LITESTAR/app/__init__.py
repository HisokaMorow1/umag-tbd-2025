from litestar import Litestar, openapi
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin, SQLAlchemySyncConfig

from app.models import Base
from app.controllers import AuthController, TagController, TodoController, UserConstroller

db_config = SQLAlchemySyncConfig(
    connection_string="sqlite:///db.sqlite3",create_all=True, metadata=Base.metadata
)

slqa_plugin = SQLAlchemyPlugin(config = db_config)

openapi_config = openapi.OpenAPIConfig(
    title="TODO API",
    version="0.9.9",
    render_plugins=[SwaggerRenderPlugin(), ScalarRenderPlugin()],
)

app = Litestar(
    route_handlers=[TodoController,UserConstroller, TagController, AuthController],openapi_config=openapi_config, plugins = [slqa_plugin],debug=True
)

