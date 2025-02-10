from pydantic_settings import BaseSettings, SettingsConfigDict

class SettingsConfigEnv(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    JWT_SECRET_ACCESS_KEY: str = 'rahasia_session'
    JWT_SECRET_REFRESH_KEY: str = 'rahasia_refresh'
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAY: int = 30
    DATABASE_URL_MYSQL: str = "mysql+aiomysql://root:@localhost:3306/mydatabase"
    DATABASE_URL_SQLITE: str = "sqlite+aiosqlite:///./test.db"
    ENCRYPTION_PASSWORD: str = "securepassword"  # Use a secure and secret password
    SALT: str = "static_salt_value"  # Salt for KDF, ideally unique per file
settings = SettingsConfigEnv()
