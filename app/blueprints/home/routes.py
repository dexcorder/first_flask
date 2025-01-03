from flask import render_template
from app.blueprints.home import home_bp

@home_bp.route('/', methods=['GET'])
def index():
    return render_template('home/index.html')  # 템플릿 파일을 렌더링