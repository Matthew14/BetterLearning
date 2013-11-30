from flask.ext.wtf import Form

from wtforms import TextField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    nameField = TextField('name', validators=[Required()])
    pwordField = PasswordField('password', validators=[Required()])

class AddStudentForm(Form):
    nameField = TextField('name', validators=[Required()])
    pwordField = PasswordField('password', validators=[Required()])
