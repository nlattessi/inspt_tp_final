from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MenuCategoriaForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class MenuItemForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio = DecimalField('Precio', validators=[DataRequired()])
    categoria_id = SelectField('Categoria', coerce=int)
    submit = SubmitField('Guardar')