#!/usr/bin/env/python3
# -*-coding: utf-8 -*-

from flask import Flask
from blog.blueprints.admin import admin_bp
from blog.blueprints.blog import blog_bp
from blog.db import db
from blog.config import Config
from blog.models import Links, Category

def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)
    app.config.from_object(Config())
    db.init_app(app)
    register_template_context(app)
    return app

def register_template_context(app):
    @app.context_processor
    def make_template_context():
        links = Links.query.order_by(Links.id).all()
        categories = Category.query.order_by(Category.name).all()
        return dict(links=links, categories=categories)

myapp = create_app()

if __name__ == '__main__':
    myapp.run(debug=True)


