from flask import Flask, session, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms import Form
from wtforms.validators import DataRequired

SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)
class SimpleForm(Form):
    example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])


@app.route('/',methods=['post','get'])
def hello_world():
    form = SimpleForm()
    print (form.example.data)
    print (form.errors)
    return render_template('RadioFormExample.html',form=form)

#SubmitRadioFormExample
@app.route("/SubmitRadioFormExample",methods=['POST','GET'])
def SubmitRadioFormExample():
    subtitle="Your Stars"
    option = request.form['options']
    return render_template("SubmitRadioFormExample.html", subtitle=subtitle,
        option=option)
