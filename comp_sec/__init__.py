import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # apply the blueprints to the app
    from comp_sec import home, enc0, enc1, enc2, enc3, enc4

    app.register_blueprint(enc0.bp)
    app.register_blueprint(enc1.bp)
    app.register_blueprint(enc2.bp)
    app.register_blueprint(enc3.bp)
    app.register_blueprint(enc4.bp)
    app.register_blueprint(home.bp)

    # makes trade/ = /
    app.add_url_rule("/", endpoint="index")

    return app
