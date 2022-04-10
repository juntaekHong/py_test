from flask import Flask,render_template, request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('youweb_1.html')


@app.route('/seulgi_2/')
def second():
    _id = request.args.get("id")
    _pass = request.args.get("pass")
    print(_id, _pass)
    return render_template('youweb_2.html',id=_id , _pass=_pass)
    #if _id == "asd" and _pass=="qwe":
    #    return render_template('second.html')
    #else:
    #    return "로그인에 실패하였습니다."
    #    return render_template("")
            

@app.route('/third/', methods=["POST"])
def third():
    _id = request.form['id']
    _password = request.form['pass']
    print(_id,_password)
    return "Hello"

@app.route('/seulgi_2/<image_file>')
def image(image_file):
    return render_template(image_file='real1/')

app.run