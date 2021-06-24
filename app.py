from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.string(30), nullable = False)
    last_name = db.Column(db.string(30), nullable = False)
    date_of_birth = db.Column(db.DateTime, )
    email = db.Column(db.string(50))
    username = db.Column(db.string(30), unique = True)
    password = db.Column(db.string(30), unique = True)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    time = 
    description = 
    experience_enjoyability = 

class UserExperience(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'), nullable = False)


if __name__ == "__main__":
    app.run(debug=True)
    