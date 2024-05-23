import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL_DESARROLLO_ALARMAS = os.getenv("DATABASE_URL_DESARROLLO_ALARMAS")
    DATABASE_URL_DESARROLLO_ORDENES = os.getenv("DATABASE_URL_DESARROLLO_ORDENES")
    DATABASE_URL_DESARROLLO_DATA_VELAS = os.getenv("DATABASE_URL_DESARROLLO_DATA_VELAS")
    APIURL = os.getenv("APIURL")
    APIKEY = os.getenv("APIKEY")
    SECRETKEY = os.getenv("SECRETKEY")

settings = Settings()