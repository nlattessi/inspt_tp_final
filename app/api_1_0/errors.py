from flask import jsonify


def bad_request(mensaje):
    response = jsonify({'status': 'bad request', 'mensaje': mensaje})
    response.status_code = 400
    return response