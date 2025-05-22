from app.models import Base
from app.config import settings

from litestar.plugins.sqlalchemy import SQLAlchemySyncConfig


db_config = SQLAlchemySyncConfig(
    connection_string=settings.database_url,create_all=True, metadata=Base.metadata
)