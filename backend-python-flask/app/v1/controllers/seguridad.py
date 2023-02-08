from ..data.usuario import UsuarioData


def login(username, password):
    
    # if (username == "admin" and password == "q1w2e3r4"):
    #     rtn = {
    #         'ok': True,
    #         'data': {
    #             'token': 'asdf34g453h45jn64j47jj5346j3456j467j467j46j7'
    #         }
    #     }
    # else:
    #     rtn = {'ok': False}

    dusuario = UsuarioData()
    usuario = dusuario.obtener(username)

    valido = False
    if (usuario is not None):
        if (usuario['password'] == password):
            valido = True

    token = ""
    if (valido):
        token = dusuario.generarToken(username)

    rtn = {
        'ok': valido,
        'token': token
    }
    
    return rtn