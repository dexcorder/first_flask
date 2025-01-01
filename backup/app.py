import threading
from flask import Flask, render_template

app = Flask(__name__)

# 플래그 변수와 락(lock) 사용
request_count = 0
request_lock = threading.Lock()

@app.before_request
def log_before_request():
    global request_count
    with request_lock:
        if request_count == 0:
            print("새로고침을 시작합니다.")
        request_count += 1

@app.after_request
def log_after_request(response):
    global request_count
    with request_lock:
        request_count -= 1
        if request_count == 0:
            print("새로고침이 완료되었습니다.")
    return response

@app.route("/")
def home():
    return render_template("index.html")  # templates 폴더에 있는 index.html 사용

@app.route("/register")
def register():
    return render_template("register.html")  #templates 폴더에 있는 register.html 사용

if __name__ == "__main__":
    app.run(debug=True)
