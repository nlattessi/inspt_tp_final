from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DecimalField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Optional, NumberRange


class ItemForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(1, 128)])
    precio = DecimalField('Precio', validators=[Optional(), NumberRange(min=0, message="El minimo es $0")], default=0)
    categoria_id = SelectField('Categoria', coerce=int)
    descripcion = TextAreaField('Descripcion', validators=[Optional()])
    submit = SubmitField('Guardar')

    def from_model(self, item):
        self.nombre.data = item.nombre
        self.precio.data = item.precio
        self.categoria_id.data = item.categoria_id
        self.descripcion.data = item.descripcion

    def to_model(self, item):
        item.nombre = self.nombre.data
        item.precio = self.precio.data
        item.categoria_id = self.categoria_id.data
        item.descripcion = self.descripcion.data