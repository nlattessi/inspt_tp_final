#################
#### imports ####
#################

from flask import flash, redirect, session, url_for, render_template, request, Blueprint
from flask.ext.login import login_required
from .. import db
from .forms import MenuCategoriaForm, MenuItemForm
from ..models import MenuItem, MenuCategoria

################
#### config ####
################

menu_blueprint = Blueprint(
    'menu', __name__,
    template_folder='templates'
)


@menu_blueprint.route('/menu')
@login_required
def index():
    categorias = db.session.query(MenuCategoria).all()
    return render_template('menu.html', categorias=categorias)


@menu_blueprint.route('/menu/<int:id>')
@login_required
def menu(id):
    categorias = db.session.query(MenuCategoria).all()
    items = MenuItem.query.filter_by(categoria_id=id).all()
    return render_template('menu.html', id=id, categorias=categorias, items=items)


@menu_blueprint.route('/menu/categorias')
@login_required
def categorias():
    categorias = db.session.query(MenuCategoria).all()
    next = url_for('menu.categorias')
    return render_template('categorias.html', categorias=categorias, next=next)


@menu_blueprint.route('/menu/categoria/agregar', methods=['GET', 'POST'])
@login_required
def categoria_agregar():
    form = MenuCategoriaForm()
    if form.validate_on_submit():
        categoria = MenuCategoria(form.nombre.data)
        db.session.add(categoria)
        db.session.commit()
        flash("La categoria " + categoria.nombre + " ha sido agregada.")
        return redirect(url_for('menu.categorias'))
    return render_template('categoria_agregar.html', form=form)


@menu_blueprint.route('/menu/categoria/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def categoria_editar(id):
    categoria = MenuCategoria.query.get_or_404(id)
    form = MenuCategoriaForm(obj=categoria)
    if form.validate_on_submit():
        categoria.nombre = form.nombre.data
        db.session.add(categoria)
        db.session.commit()
        flash("La categoria " + categoria.nombre + " ha sido editada.")
        return redirect(url_for('menu.categorias'))
    return render_template('categoria_editar.html', form=form)


@menu_blueprint.route('/menu/categoria/borrar/<int:id>', methods=['POST'])
@login_required
def categoria_borrar(id):
    if request.method == 'POST':
        categoria = MenuCategoria.query.get_or_404(id)
        items = MenuItem.query.filter_by(categoria_id=id).all()
        for item in items:
            item.categoria_id = None
            db.session.add(item)
        db.session.delete(categoria)
        db.session.commit()
        flash("La categoria " + categoria.nombre + " ha sido borrada.")
        return redirect(request.referrer)
    return redirect(url_for('menu.index'))


@menu_blueprint.route('/menu/items')
@login_required
def items():
    items = db.session.query(MenuItem).all()
    return render_template('items.html', items=items)


@menu_blueprint.route('/menu/item/agregar', methods=['GET', 'POST'])
@login_required
def item_agregar():
    form = MenuItemForm()
    form.categoria_id.choices = [(c.id, c.nombre) for c in MenuCategoria.query.order_by('nombre')]
    if form.validate_on_submit():
        item = MenuItem(
            form.nombre.data,
            form.precio.data,
            form.categoria_id.data)
        db.session.add(item)
        db.session.commit()
        flash("El item " + item.nombre + " ha sido agregado.")
        return redirect(url_for('menu.items'))
    return render_template('item_agregar.html', form=form)


@menu_blueprint.route('/menu/item/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def item_editar(id):
    item = MenuItem.query.get_or_404(id)
    form = MenuItemForm(obj=item)
    form.categoria_id.choices = [(c.id, c.nombre) for c in MenuCategoria.query.order_by('nombre')]
    if form.validate_on_submit():
        item.nombre = form.nombre.data
        item.precio = form.precio.data
        item.categoria_id = form.categoria_id.data
        db.session.add(item)
        db.session.commit()
        flash("El item " + item.nombre + " ha sido editado.")
        return redirect(url_for('menu.items'))
    return render_template('item_editar.html', form=form)


@menu_blueprint.route('/menu/item/borrar/<int:id>', methods=['POST'])
@login_required
def item_borrar(id):
    if request.method == 'POST':
        item = MenuItem.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash("El item " + item.nombre + " ha sido borrado.")
        return redirect(request.referrer)
    return redirect(url_for('menu.index'))