from flask import Flask
from app.config import Config
from app.main import main 
from app.alarms import alarms 
from app.bingx import bingx 
from app.logging import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos
    from app.alarms.util import init_db
    init_db()

    # Registro de Blueprints
    app.register_blueprint(main)
    app.register_blueprint(alarms, url_prefix='/alarms')
    app.register_blueprint(bingx, url_prefix='/bingx')
    app.register_blueprint(logging, url_prefix='/logs')

    return app
