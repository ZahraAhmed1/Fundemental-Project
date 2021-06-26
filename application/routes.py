from flask import render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


from application import app, db

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/signup', methods = ['GET','POST'])
def signup():
    error = ""
    form = UserForm()

    if request.method == 'POST' :
        first_name = form.first_name.data
        last_name = form.last_name.date
        date_of_birth = form.date_of_birth.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username) == 0 or len(password) == 0:
            error = "Please fill in all boxes"
        elif len(YYYY) < 4 or len(MM) > 2 or len(DD) > 2 :
            error = "Please enter your date of birth as YYYY-MM-DD"
        else:
            return "Sign up successful"    

    return render_template('home.html', form = form, message = error)





