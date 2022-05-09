from ensurepip import bootstrap
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bs = Bootstrap5(app)

@app.route('/')
def hello_world():
    return render_template('index.html')