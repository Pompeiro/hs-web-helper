import typing as T

from pydantic import BaseSettings


class Settings(BaseSettings):
    allowed_origins: T.List[str]
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str


settings = Settings()
