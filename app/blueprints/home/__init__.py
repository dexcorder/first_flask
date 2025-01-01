from flask import Blueprint

home_bp = Blueprint('home', __name__, template_folder='templates')

# routes.py를 명시적으로 가져옵니다.
from app.blueprints.home import routes