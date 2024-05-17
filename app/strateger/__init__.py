from flask import Blueprint

strateger = Blueprint('strateger', __name__)

from app.strateger import routes  # Asegúrate de que esto esté presente