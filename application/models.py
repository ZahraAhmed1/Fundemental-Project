from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    date_of_birth = db.Column(db.Date)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(30))
    # userexperience = db.relationship('UserExperience', backref = 'user')

class Experiences(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    kind = db.Column(db.String(50), nullable = False)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    experience_enjoyability = db.Column(db.String(10))
    # userexperience = db.relationship('UserExperience', backref = 'experience')

# class UserExperience(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
#     experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'), nullable = False) 
