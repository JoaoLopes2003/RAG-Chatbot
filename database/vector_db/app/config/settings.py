from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_db_host: str
    mongo_db_port: int
    mongo_db_name: str

    api_key: str

    @property
    def mongo_connection_string(self) -> str:
        return f"mongodb://{self.mongo_db_host}:{self.mongo_db_port}"

    class Config:
        # Get the environment variables
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()