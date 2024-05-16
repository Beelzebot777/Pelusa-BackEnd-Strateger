from flask import Flask
from app.config import Config
from app.main import main 
from app.alarms import alarms 
from app.bingx import bingx 
from app.logging import logging

from app.logging.models import init_db_logs_tbl_alarms, init_db_logs_tbl_trades

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos    
    init_db_logs_tbl_alarms()
    init_db_logs_tbl_trades()

    # Registro de Blueprints 
    app.register_blueprint(main)
    app.register_blueprint(alarms, url_prefix='/alarms')
    app.register_blueprint(bingx, url_prefix='/bingx')
    app.register_blueprint(logging, url_prefix='/logs')

    return app
