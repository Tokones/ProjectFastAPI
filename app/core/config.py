from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    db_dir: Path = Path(__file__).resolve().parents[2] / "app" / "models"
    db_path: Path = db_dir / "database.db"
    jwt_secret: str
    jwt_algorithm: str
    jwt_expire_minutes: int

    class Config:
        env_file = str(Path(__file__).parent / ".env")

settings = Settings()