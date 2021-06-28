from flask import Flask, render_template, url_for, request 
from flask_wtf import FlaskForm
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, DateField, PasswordField
from application.models import Experiences,Users
from application.forms import UsersForm, UpdateUsersForm
from wtforms.validators import data_required
from application import app, db




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = UsersForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = Users(first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,email=email,username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', form = form)


@app.route('/update', methods = ['GET','POST'])
def update():
    form = UpdateUsersForm()
    user = Users.query.get(id)
    if form.validate_on_submit():
        password = form.new_password.data
        if password:
            user.password=password
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('update.html', form = form)

@app.route('/delete')
def delete(id=None):
    if id == None:
        return "No user found "
    else:
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
    return render_template('home.html') 

@app.route('/read')
def read():
    # experiences = Experiences.query.all()
    return render_template('read.html')