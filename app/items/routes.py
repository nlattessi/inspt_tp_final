from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required, current_user
from . import items
from .forms import ItemForm
from .. import db
from ..models import Item, Categoria
from ..utils import get_redirect_target, redirect_back


@items.route('/')
@login_required
def get_all():
    items = Item.query.order_by(Item.nombre.desc()).all()
    return render_template('items/index.html', items=items)


@items.route('/<int:id>')
@login_required
def get(id):
    item = Item.query.get_or_404(id)
    return render_template('items/item.html', item=item)


@items.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ItemForm()
    form.categoria_id.choices = [(c.id, c.nombre) for c in Categoria.query.order_by(Categoria.nombre.desc())]
    if form.validate_on_submit():
        item = Item(nombre=form.nombre.data, precio=form.precio.data, descripcion=form.descripcion.data, categoria_id=form.categoria_id.data)
        db.session.add(item)
        db.session.commit()
        flash("El item ha sido agregado.", 'success')
        return redirect(url_for('.get', id=item.id))
    return render_template('items/edit.html', form=form, titulo_pag="Agregar")


@items.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    item = Item.query.get_or_404(id)
    if not current_user.is_admin:
        abort(403)
    form = ItemForm()
    form.categoria_id.choices = [(c.id, c.nombre) for c in Categoria.query.order_by(Categoria.nombre.desc())]
    if form.validate_on_submit():
        form.to_model(item)
        db.session.add(item)
        db.session.commit()
        flash("El item ha sido actualizado.", 'success')
        return redirect(url_for('.get', id=item.id))
    form.from_model(item)
    return render_template('items/edit.html', form=form, titulo_pag="Editar")


@items.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    item = Item.query.get_or_404(id)
    if not current_user.is_admin:
        abort(403)
    next = get_redirect_target()
    if request.method == 'POST':
        if request.form['btn'] == "Si":
            db.session.delete(item)
            db.session.commit()
            flash("El item ha sido borrado.", 'success')
        else:
            return redirect_back('items.get_all')
        return redirect(url_for('.get_all'))
    return render_template('items/delete.html', item=item, next=next)