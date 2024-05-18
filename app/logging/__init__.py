from flask import Blueprint

logging = Blueprint('logging', __name__, template_folder='templates')

from app.logging import routes
