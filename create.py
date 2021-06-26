from application import db

db.drop_all()
db.create_all()



# from app import db, Users, Experiences, UserExperience

# db.drop_all()
# db.create_all() # Creates all table classes defined

# user_1 = Users(first_name(''))
# user_2 = Users(first_name(''))
# user_3 = Users(first_name(''))
# user_4 = Users(first_name(''))
# user_5 = Users(first_name(''))

# db.session.add(user_1)
# db.session.add(user_2)
# db.session.add(user_3)
# db.session.add(user_4)
# db.session.add(user_5)
# db.session.commit()
