from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')

# routes.py를 명시적으로 가져옵니다.
from app.blueprints.auth import routes