#!/usr/bin/env/python3
# -*-coding: utf-8 -*-

from flask import Flask
from blog.admin import bp
from blog.db import db
from blog.config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config.from_object(Config())
    db.init_app(app)
    return app

myapp = create_app()
if __name__ == '__main__':
    myapp.run(debug=True)