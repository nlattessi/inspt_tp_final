from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CategoriaForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])


class ItemForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])
    #precio = IntegerField('Precio', validators=[DataRequired()])
    precio = DecimalField('Precio', validators=[DataRequired()])
    categoria_id = SelectField('Categoria', coerce=int)



# class UserDetails(Form):
#     group_id = SelectField(u'Group', coerce=int)

# def edit_user(request, id):
#     user = User.query.get(id)
#     form = UserDetails(request.POST, obj=user)
#     form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]