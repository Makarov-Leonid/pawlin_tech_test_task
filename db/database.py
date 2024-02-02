from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import DBSettings

project_engine = create_engine(
    url=DBSettings.db_url_psycopg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

session_fact = sessionmaker(project_engine)


class BaseOrm(DeclarativeBase):
    pass
