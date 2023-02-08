from flask import Blueprint, jsonify


producto_api = Blueprint('producto', __name__)

@producto_api.route('/listado', methods=['GET'])
def producto_listado():
    arr = [{'id': 1, 'nombre': 'pelota futbol', 'precio': 70.60 }, {'id': 2, 'nombre': 'pelota tenis', 'precio': 90.60 }]

    rtn = {
        'ok': True,
        'data': arr
    }

    return (jsonify(rtn), 200)

@producto_api.route('/nuevo', methods=['POST'])
def producto_nuevo():

    id = 0

    rtn = {
        'ok': True,
        'data': id
    }

    return (jsonify(rtn), 200)
    
@producto_api.route('/editar/<id>', methods=['POST'])
def producto_editar(id):
    
    rtn = {
        'ok': True,
        'data': id
    }

    return (jsonify(rtn), 200)