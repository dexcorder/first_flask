import threading

# 플래그 변수와 락(lock) 사용
request_count = 0
request_lock = threading.Lock()

def init_logging(app):
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