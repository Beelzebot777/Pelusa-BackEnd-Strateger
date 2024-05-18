from flask import Blueprint

bingx = Blueprint('bingx', __name__, template_folder='templates')

from app.bingx import routes
