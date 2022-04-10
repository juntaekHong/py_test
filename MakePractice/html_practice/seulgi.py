from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('youweb_1.html')

@app.route('/seulgi_p/')
def picture():
    return render_template("seulgi's_picture.html")

app.run()