# Path: app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL_DESARROLLO_ALARMAS = os.getenv("DATABASE_URL_DESARROLLO_ALARMAS").replace("pymysql", "aiomysql")
    DATABASE_URL_DESARROLLO_ORDENES = os.getenv("DATABASE_URL_DESARROLLO_ORDENES").replace("pymysql", "aiomysql")
    DATABASE_URL_DESARROLLO_DATA_VELAS = os.getenv("DATABASE_URL_DESARROLLO_DATA_VELAS").replace("pymysql", "aiomysql")
    APIURL = os.getenv("APIURL")
    APIKEY = os.getenv("APIKEY")
    SECRETKEY = os.getenv("SECRETKEY")
    ALLOWED_IPS = os.getenv("ALLOWED_IPS", "").split(",")
    BLOCKED_IPS = os.getenv("BLOCKED_IPS", "").split(",")    

settings = Settings()

