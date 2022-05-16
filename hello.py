from ensurepip import bootstrap
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields import FileField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bs = Bootstrap5(app)
app.config['SECRET_KEY']= '#sEcReTkEy!2220'

class FileForm(FlaskForm):
    name = FileField('Select a File to Upload',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/analyzer',methods=['GET','POST'])
def analyzer_page():
    name = None
    form = FileForm()
    return render_template('analyzer.html',form=form,name=name)