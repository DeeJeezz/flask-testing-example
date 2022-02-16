from collections import defaultdict
import logging

from flask import Flask


def create_app():
    app: Flask = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)

    app.config['pages'] = defaultdict(int)

    import routes  # noqa
    app.register_blueprint(routes.routes_bp)

    return app
