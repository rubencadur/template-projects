from flask import Flask, jsonify
from .config import app_config
from flask_cors import CORS
from .v1 import attach_apis as v1_attach_apis


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    CORS(app, resources={r"/*": {"origins": "*"}})


    app = v1_attach_apis(app)


    @app.errorhandler(404)
    def page_not_found(err):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(405)
    def page_not_authorized(err):
        return jsonify({'error': 'Not authorized'}), 405

    return app
