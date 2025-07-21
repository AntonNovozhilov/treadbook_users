from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    """Настройки приложения."""

    db_port: int
    db_host: str
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"
        env_prefix = "user_"


settings = Setting()
