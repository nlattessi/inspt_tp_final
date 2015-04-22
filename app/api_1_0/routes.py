from flask import jsonify
from . import api
from .errors import bad_request
from ..models import Categoria


@api.route('/categorias', methods=['GET'])
def get_categorias():
    categorias = Categoria.query.order_by(Categoria.nombre.desc()).all()
    json_results = []
    for categoria in categorias:
        json_item = []
        for item in categoria.items:
            i = {
                'id': item.id,
                'nombre': item.nombre,
                'descripcion': item.descripcion
            }
            json_item.append(i)
        c = {
            'id': categoria.id,
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
            'items': json_item
        }
        json_results.append(c)
    return jsonify(categorias=json_results)
