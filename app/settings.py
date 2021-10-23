from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite:///./database.sqlite3"


settings = Settings()
