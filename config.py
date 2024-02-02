__all__ = ["PostgreSQLSettings"]

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgreSQLSettings(BaseSettings):
    load_dotenv()

    DB_SERVER: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def db_url_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


DBSettings = PostgreSQLSettings()

if __name__ == "__main__":
    c = PostgreSQLSettings()
