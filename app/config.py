from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    NAME: str
    USER: str
    PASS: str
    HOST: str
    PORT: int

    ECHO: bool = False
    ECHO_POOL: bool = False
    POOL_SIZE: int = 50
    MAX_OVERFLOW: int = 10

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        env_nested_delimiter="__",
    )

    LOG_LEVEL: str = "INFO"
    DB: DatabaseSettings
    WORKERS: int = 2
    START_TIME_HOUR: int = 7
    END_TIME_HOUR: int = 23
    WALK_DURATION: int = 30


settings = Settings()
