# -*- coding: utf-8 -*-

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asd18f15DSFwef54"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
