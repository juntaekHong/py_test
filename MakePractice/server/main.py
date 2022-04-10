from flask import Flask

app= Flask(__name__)

@app.route('/') # - 주소 -> 127.0.0.1:5000/, localhost:5000/
                # route: 다음에 나오는 함수를 실행시키는 것

def index():
    return 'gg!'

@app.route('/jooyoung_code/') # web- address -> 127.0.0.1:5000/jooyoung_code/

def second():
    return "goal!"

app.run

