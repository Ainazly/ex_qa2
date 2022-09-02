import os
from dotenv import load_dotenv
# from pathlib import Path
load_dotenv()
# env_path = Path('.')/'.env'
# load_dotenv(dotenv_path=env_path)

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

TOKEN = os.getenv("TOKEN")