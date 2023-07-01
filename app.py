from flask import Flask,render_template,request,redirect
from db import Database
import api

app=Flask(__name__)
dbo=Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message='Email already exists')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    response=dbo.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message1="Incorrect email/password")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    response=api.ner(text)
    return render_template('ner.html',response=response)


app.run(debug=True)