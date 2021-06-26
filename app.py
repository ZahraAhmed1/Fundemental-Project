from application import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')







# from flask import Flask 
# from flask_sqlalchemy import SQLAlchemy 
# from os import getenv

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# db = SQLAlchemy(app)

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     first_name = db.Column(db.String(30), nullable = False)
#     last_name = db.Column(db.String(30), nullable = False)
#     date_of_birth = db.Column(db.DateTime)
#     email = db.Column(db.String(50))
#     username = db.Column(db.String(30), unique = True)
#     password = db.Column(db.String(30))
#     userexperience = db.relationship('UserExperience', backref = 'user')

# class Experiences(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     kind = db.Column(db.String(50), nullable = False)
#     date = db.Column(db.DateTime)
#     description = db.Column(db.String(500))
#     experience_enjoyability = db.Column(db.String(10))
#     userexperience = db.relationship('UserExperience', backref = 'experience')

# class UserExperience(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
#     experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'), nullable = False)


# if __name__ == "__main__":
#     app.run(debug=True)
    
