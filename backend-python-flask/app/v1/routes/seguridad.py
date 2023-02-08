from flask import Blueprint, jsonify, request
from flask_cors import CORS

import app.v1.controllers.seguridad as SeguridadController

seguridad_api = Blueprint('seguridad', __name__)

CORS(seguridad_api)

@seguridad_api.route('login', methods=['POST'])
def login():

    content = request.json

    username = ""
    if "username" in content:
        username = content['username']

    password = ""
    if "password" in content:
        password = content['password']


    rtn = SeguridadController.login(username, password)

    return (jsonify(rtn), 200)
    
@seguridad_api.route('reset-password', methods=['POST'])
def resetPasssword():

    rtn = {
        'ok': True
    }

    return (jsonify(rtn), 200)
    