import os
from pydantic_settings import BaseSettings

if not os.environ.get("ENV_LOADED"):
    if os.path.isfile(".env"):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["ENV_LOADED"] = "True"
        print("Loading environment variables from .env")
    else:
        print("No .env file found. Usding system environment variables")
        
        
class Config(BaseSettings):
    # General settings
    TIME_ZONE: str
    
    # PostgreSQL
    PSQL_ENGINE: str
    PSQL_NAME: str
    PSQL_USER: str
    PSQL_PASSWORD: str
    PSQL_HOST: str
    PSQL_PORT: str
    
    
config = Config()