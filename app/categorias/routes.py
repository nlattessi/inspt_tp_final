from flask import render_template, redirect, url_for, flash, abort, request
from flask.ext.login import login_required, current_user
from . import categorias
from .forms import CategoriaForm
from .. import db
from ..models import Categoria, Item
from ..utils import get_redirect_target, redirect_back


@categorias.route('/')
@login_required
def get_all():
    categorias = Categoria.query.order_by(Categoria.nombre.desc()).all()
    return render_template('categorias/index.html', categorias=categorias)


@categorias.route('/<int:id>')
@login_required
def get(id):
    categoria = Categoria.query.get_or_404(id)
    return render_template('categorias/categoria.html', categoria=categoria)


@categorias.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CategoriaForm()
    if not current_user.is_admin:
        abort(403)
    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data, descripcion=form.descripcion.data)
        db.session.add(categoria)
        db.session.commit()
        flash("La categoria ha sido agregada.", 'success')
        return redirect(url_for('.get', id=categoria.id))
    return render_template('categorias/edit.html', form=form, titulo_pag="Agregar")


@categorias.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    categoria = Categoria.query.get_or_404(id)
    if not current_user.is_admin:
        abort(403)
    form = CategoriaForm()
    if form.validate_on_submit():
        form.to_model(categoria)
        db.session.add(categoria)
        db.session.commit()
        flash("La categoria ha sido actualizada.", 'success')
        return redirect(url_for('.get', id=categoria.id))
    form.from_model(categoria)
    return render_template('categorias/edit.html', form=form, titulo_pag="Editar")


@categorias.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    categoria = Categoria.query.get_or_404(id)
    if not current_user.is_admin:
        abort(403)
    next = get_redirect_target()
    if request.method == 'POST':
        if request.form['btn'] == "Si":
            items = Item.query.filter_by(categoria_id=categoria.id).all()
            for item in items:
                item.categoria_id = None
                db.session.add(item)
            db.session.delete(categoria)
            db.session.commit()
            flash("La categoria ha sido borrada.", 'success')
        else:
            return redirect_back('categorias.get_all')
        return redirect(url_for('.get_all'))
    return render_template('categorias/delete.html', categoria=categoria)