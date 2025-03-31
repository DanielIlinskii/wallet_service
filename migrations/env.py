import sys
from pathlib import Path
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

sys.path.append(str(Path(__file__).parent.parent))

from app.models import Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata