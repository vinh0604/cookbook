from pydantic import BaseSettings

class Settings(BaseSettings):
    smtp_server: str
    smtp_port: int
    smtp_user: str
    smtp_password: str

    jwt_secret: str

    magic_link_base_url: str
    magic_link_from_email: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'