from flask import Blueprint

bingx = Blueprint('bingx', __name__)

from app.bingx import routes
