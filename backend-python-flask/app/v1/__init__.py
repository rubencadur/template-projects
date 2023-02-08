from .routes.seguridad import seguridad_api
from .routes.producto import producto_api


def attach_apis(app):

    app.register_blueprint(seguridad_api, url_prefix="/v1/seguridad")
    app.register_blueprint(producto_api, url_prefix="/v1/producto")

    return app