from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, ScalarRenderPlugin
from litestar.config.cors import CORSConfig

from app.controllers import TagController, TodoController, UserController, AuthController
from app.db import sqla_plugin
from app.security import oauth2_auth
from app.config import settings


openapi_config = OpenAPIConfig(
    title="Todo API",
    version="0.9.9",
    render_plugins=[SwaggerRenderPlugin(),ScalarRenderPlugin()])

cors_config = CORSConfig(allow_origins=["*"])

# Una lista de funciones para recibir información de la API
app = Litestar(
    route_handlers=[TodoController, UserController, TagController, AuthController], 
    openapi_config=openapi_config,
    plugins=[sqla_plugin],
    debug=settings.debug,
    cors_config=cors_config,
    #on_app_init=[oauth2_auth.on_app_init],
    #pdb_on_exception=True # Es para debuggear desde VSCode: Ejecutar>Iniciar depuración
    )