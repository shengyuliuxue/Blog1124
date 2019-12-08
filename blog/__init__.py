#!/usr/bin/env/python3
# -*-coding: utf-8 -*-

from flask import Flask
from blog.blueprints.admin import admin_bp
from blog.blueprints.blog import blog_bp
from blog.db import db
from blog.config import Config


def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)
    app.config.from_object(Config())
    db.init_app(app)
    return app

myapp = create_app()

if __name__ == '__main__':
    myapp.run(debug=True)
