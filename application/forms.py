from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms.validators import data_required

class UsersForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[data_required()])
    last_name = StringField("Last Name: ", validators=[data_required()])
    date_of_birth = DateField("Birthday(YYYY-MM-DD): ", validators=[data_required()])
    email = StringField("Email: ", validators=[data_required()])
    username = StringField("Username: ", validators=[data_required()])
    password = PasswordField("Password: ", validators=[data_required()])
    submit = SubmitField('Submit')

class UpdateUsersForm(FlaskForm):
    old_password = PasswordField("Old Password: ", validators=[data_required()])
    new_password = PasswordField("New Password: ", validators=[data_required()])
    submit = SubmitField('Update')
    