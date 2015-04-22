from flask import render_template, send_file, jsonify, request
from . import home
from ..models import User, Categoria, Item


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
                    DateField, IntegerField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
class LoginForm(Form):
    wizard_name = StringField('Wizard Name',
                              validators=[Required(), Length(1, 32)])
    password = PasswordField('Password', validators=[Required(),
                                                     Length(1, 32)])

    def validate(self):
        if not Form.validate(self):
            return False
        if not self.wizard_name.data == 'admin' or not self.password.data == 'admin':
            self.password.errors.append('Incorrect password.')
            return False
        return True


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('home/user.html', user=user)


@home.route('/pruebas3', methods=['GET', 'POST'])
def pruebas3():
    form = LoginForm()
    if form.validate_on_submit():
        if form.wizard_name.data == 'admin' and form.password.data == 'admin':
            return redirect(url_for('home.pruebas3_landing'))
    return render_template('home/pruebas3.html', form=form, no_nav=True)


@home.route('/pruebas')
def pruebas():
    return render_template('home/pruebas.html')

@home.route('/pruebas2', methods=['GET', 'POST'])
def pruebas2():
    categorias = Categoria.query.order_by(Categoria.nombre.desc()).all()
    if request.method == 'POST':
        info = request.form.getlist('item')
        item = Item.query.get_or_404(info)
        print(info)
        return render_template('home/pruebas2.html', categorias=categorias, info=info, item=item)
    else:
        categorias = Categoria.query.order_by(Categoria.nombre.desc()).all()
        return render_template('home/pruebas2.html', categorias=categorias)

@home.route('/jsondata/data.json')
def send_json():
    categorias = Categoria.query.order_by(Categoria.nombre.desc()).all()
    list = [
        {
            "beverages": "Coffee,Coke",
            "snacks": "Chips,Cookies"
        }
    ]
    json_results = []
    for cat in categorias:
        c = {}
        c['id'] = cat.id
        c['nombre'] = cat.nombre
        c['descripcion'] = cat.descripcion
        json_results.append(c)
    return jsonify(data=json_results)
    #return send_file('home/data.json')

@home.route('/json', methods=['GET', 'POST'])
def jsonget():
    if request.method == 'POST':
        select = request.form.getlist('item')
        print(select)
    else:
        cat_id = request.args.get('cat_id', 0, type=int)
        categoria = Categoria.query.get_or_404(cat_id)
        json_results = []
        for item in categoria.items:
            i = {
                'id': item.id,
                'nombre': item.nombre,
                'descripcion': item.descripcion
            }
            json_results.append(i)
        return jsonify(items=json_results)

@home.route('/json/<int:cat_id>', methods=['GET'])
def json_cat(cat_id):
    categoria = Categoria.query.get_or_404(cat_id)
    json_results = []
    for item in categoria.items:
        i = {
            'id': item.id,
            'nombre': item.nombre,
            'descripcion': item.descripcion
        }
        json_results.append(i)
    return jsonify(items=json_results)
    # for categoria in categorias:
    #     json_item = []
    #     for item in categoria.items:
    #         i = {
    #             'id': item.id,
    #             'nombre': item.nombre,
    #             'descripcion': item.descripcion
    #         }
    #         json_item.append(i)
    #     c = {
    #         'id': categoria.id,
    #         'nombre': categoria.nombre,
    #         'descripcion': categoria.descripcion,
    #         'items': json_item
    #     }
    #     json_results.append(c)
    # return jsonify(categorias=json_results)