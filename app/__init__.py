from flask import Flask
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    bcrypt.init_app(app)

    # Blueprint 등록
    from app.blueprints.auth import auth_bp
    from app.blueprints.home import home_bp
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(home_bp, url_prefix='/')  # '/' URL에 연결

    return app
