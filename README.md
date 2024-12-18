# Flask 프로젝트 설정 안내

이 프로젝트는 Flask를 기반으로 개발되었으며, 가상환경과 `requirements.txt`를 이용해 쉽게 개발 환경을 구성할 수 있습니다.

## 1. 개발 환경 설정

### 1.1 Python 가상환경 생성
프로젝트의 의존성을 독립적으로 관리하기 위해 Python 가상환경을 생성합니다.

#### **Windows 환경**
1. 프로젝트 폴더로 이동합니다:
   ```bash
   cd flask_project
   ```
2. Python 가상환경을 생성합니다:
   ```bash
   python -m venv env
   ```
3. 가상환경을 활성화합니다:
   ```bash
   env\Scripts\activate
   ```
   활성화되면 프롬프트에 `(env)`가 표시됩니다.

#### **Linux/macOS 환경**
1. 프로젝트 폴더로 이동합니다:
   ```bash
   cd flask_project
   ```
2. Python 가상환경을 생성합니다:
   ```bash
   python3 -m venv env
   ```
3. 가상환경을 활성화합니다:
   ```bash
   source env/bin/activate
   ```
   활성화되면 프롬프트에 `(env)`가 표시됩니다.

---

### 1.2 의존성 설치
가상환경이 활성화된 상태에서 `requirements.txt`를 이용해 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

> **Tip:** `requirements.txt` 파일은 프로젝트에 필요한 패키지와 버전을 명시하고 있습니다.

---

## 2. Flask 애플리케이션 실행
1. 가상환경이 활성화된 상태에서 프로젝트의 메인 파일 `app.py`를 실행합니다:
   ```bash
   python app.py
   ```
2. 서버가 정상적으로 실행되면 다음과 같은 메시지가 표시됩니다(port 5000은 예시입니다):
   ```
   * Running on http://127.0.0.1:5000/
   ```
3. 브라우저를 열고 `http://127.0.0.1:5000/`에 접속하면 애플리케이션을 확인할 수 있습니다.

---

## 3. 가상환경 비활성화
- 프로젝트 종료 하고 싶을 때는
  CTRL + C

- 작업이 끝난 후 가상환경을 비활성화하려면 다음 명령어를 실행합니다:

```bash
deactivate
```

---

## 4. 추가 정보
- 프로젝트 의존성 추가 시:
   ```bash
   pip install <패키지명>
   pip freeze > requirements.txt
   ```
   위 명령어를 통해 의존성 파일(`requirements.txt`)을 업데이트할 수 있습니다.

- 오류나 궁금한 점이 있으면 함께 공부해봅시다!

---

**Happy Coding! 🚀**
