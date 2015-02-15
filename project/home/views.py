#################
#### imports ####
#################

from flask import flash, redirect, session, url_for, render_template, request, Blueprint
from flask.ext.login import login_required
from project import db
from project.models import MenuItem, MenuCategoria
from .forms import CategoriaForm, ItemForm

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

# class UserDetails(Form):
#     group_id = SelectField(u'Group', coerce=int)

# def edit_user(request, id):
#     user = User.query.get(id)
#     form = UserDetails(request.POST, obj=user)
#     form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]


@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form_categoria = CategoriaForm(prefix="form_categoria")
    form_item = ItemForm(prefix="form_item")
    form_item.categoria_id.choices = [(c.id, c.nombre) for c in MenuCategoria.query.order_by('nombre')]
    if form_categoria.validate_on_submit() and form_categoria.nombre.data:
        nueva_categoria = MenuCategoria(form_categoria.nombre.data)
        db.session.add(nueva_categoria)
        db.session.commit()
        flash('Una nueva categoria ha sido agregada.')
        return redirect(url_for('home.home'))
    elif form_item.validate_on_submit() and form_item.nombre.data:
        nuevo_item = MenuItem(form_item.nombre.data, form_item.precio.data, form_item.categoria_id.data)
        db.session.add(nuevo_item)
        db.session.commit()
        flash('Un nuevo item ha sido agregado')
        return redirect(url_for('home.home'))
    else:
        menu_items = db.session.query(MenuItem).all()
        return render_template('index.html', menu_items=menu_items, form_categoria=form_categoria, form_item=form_item)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')


# @home_blueprint.route('/categoria', methods=['GET', 'POST'])
# def register():
#     #form = RegisterForm(request.form)
#     form = RegisterForm()
#     #if request.method == 'POST':
#     if form.validate_on_submit():
#         user = User(
#             username=form.username.data,
#             email=form.email.data,
#             password=form.password.data
#         )
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return redirect(url_for('home.home'))
#     return render_template('register.html', form=form)