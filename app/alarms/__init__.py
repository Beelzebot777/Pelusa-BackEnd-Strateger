from flask import Blueprint

alarms = Blueprint('alarms', __name__, template_folder='templates')

from app.alarms import routes
