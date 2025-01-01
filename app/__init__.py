from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트 등록
    from .routes.home import home_bp
    from .routes.auth import auth_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    # 새로고침 로깅 초기화
    from .utils.logging import init_logging
    init_logging(app)

    return app