from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    #username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Seguir conectado')
    submit = SubmitField('Log in')


class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Registrar!')