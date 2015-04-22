from flask import render_template
from . import pedidos


@pedidos.route('/')
def index():
    return render_template('pedidos/index.html')