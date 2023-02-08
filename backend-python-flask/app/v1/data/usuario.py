import mysql.connector
from mysql.connector import Error
from os import getenv
from .dataaccess import DataAccess


class UsuarioData(DataAccess):

    def obtener(self, username):
        usuario = None

        procedure = "usp_usuario_s_usuario"
        parametros = [username]

        data = self.ExecuteSelectProdure(procedure, parametros)
        arr = data['result']
        #args = data['params']
        if (arr and len(arr) > 0):
            if (len(arr[0]) > 0):
                usuario = arr[0][0]

        return usuario

    def generarToken(self, username):
        token = ""

        procedure = "usp_usuario_s_generarToken"
        parametros = [username, '']

        data = self.ExecuteProdure(procedure, parametros)
        args = data['params']
        if (args):
            token = args[1]

        return token