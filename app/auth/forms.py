from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from ..models import User


def name_exists(form, field):
    user = User.query.filter_by(username=field.data).first()
    if user:
        raise ValidationError('Usuario con ese nombre ya existe.')


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Seguir conectado')
    submit = SubmitField('Log in')


class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=1, max=64),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username debe ser 1 palabra, solo letras, "
                         "numeros y guion bajo.")
            ),
            name_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, max=25)
        ]
    )
    confirm = PasswordField(
        'Repetir password',
        validators=[
            DataRequired(),
            EqualTo('password', message="Passwords deben coincidir.")
        ]
    )
    is_admin = BooleanField('Es admin?')
    submit = SubmitField('Registrar!')
