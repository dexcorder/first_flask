from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # templates 폴더에 있는 index.html 사용

if __name__ == "__main__":
    app.run(debug=True)
