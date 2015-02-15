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

menu_blueprint = Blueprint(
    'menu', __name__,
    template_folder='templates'
)


@menu_blueprint.route('/menu')
@login_required
def menu():
    menu_items = db.session.query(MenuItem).all()
    return render_template('menu.html', menu_items=menu_items)

@menu_blueprint.route('/menu/categoria', methods=['GET', 'POST'])
@login_required
def categoria():
    form = CategoriaForm()
    if form.validate_on_submit():
        categoria = MenuCategoria(form.nombre.data)
        db.session.add(categoria)
        db.session.commit()
        flash('Una nueva categoria ha sido agregada.')
        return redirect(url_for('menu.menu'))
    return render_template('categoria.html', form=form)

@menu_blueprint.route('/menu/item', methods=['GET', 'POST'])
@login_required
def item():
    form = ItemForm()
    form.categoria_id.choices = [(c.id, c.nombre) for c in MenuCategoria.query.order_by('nombre')]
    if form.validate_on_submit():
        item = MenuItem(
            form.nombre.data,
            form.precio.data,
            form.categoria_id.data)
        db.session.add(item)
        db.session.commit()
        flash('Un nuevo item ha sido agregado')
        return redirect(url_for('menu.menu'))
    return render_template('item.html', form=form)
