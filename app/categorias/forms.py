from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

class CategoriaForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(1, 128)])
    descripcion = TextAreaField('Descripcion', validators=[Optional()])
    submit = SubmitField('Guardar')

    def from_model(self, categoria):
        self.nombre.data = categoria.nombre
        self.descripcion.data = categoria.descripcion

    def to_model(self, categoria):
        categoria.nombre = self.nombre.data
        categoria.descripcion = self.descripcion.data