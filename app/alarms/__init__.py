from flask import Blueprint

alarms = Blueprint('alarms', __name__)

from app.alarms import routes
