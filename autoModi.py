import os
import re

# HTML 파일들이 있는 디렉토리
html_dir = "./templates"
 
# 정적 파일 경로 패턴 (예: /static/css/style.css) 
    # https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">    
    # <link rel="stylesheet" href="assets/css/styles.css">
    # <link rel="stylesheet" href="node_modules/swiper/swiper-bundle.css">
    # <link rel="stylesheet" href="assets/css/custom.css">

pattern = r'^\/node_modules\/.*\.(css|js)$'

# HTML 파일 경로 순회
for root, dirs, files in os.walk(html_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # 경로를 url_for로 변경
            new_html_content = re.sub(pattern, r'{{ url_for("static", filename="\1") }}', html_content)

            # 변경된 내용을 다시 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_html_content)

print("경로 변경 완료!")
