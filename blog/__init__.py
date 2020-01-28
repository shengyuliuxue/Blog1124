#!/usr/bin/env/python3
# -*-coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
login_manager = LoginManager()
from blog.blueprints.admin import admin_bp
from blog.blueprints.blog import blog_bp
from blog.db import db
from blog.config import Config
from blog.models import Links, Category
import click



def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)
    app.config.from_object(Config())
    db.init_app(app)
    register_template_context(app)
    app.secret_key = 'shengyu'
    login_manager.init_app(app)
    return app

def register_template_context(app):
    @app.context_processor
    def make_template_context():
        links = Links.query.order_by(Links.id).all()
        categories = Category.query.order_by(Category.name).all()
        return dict(links=links, categories=categories)

myapp = create_app()

#def register_commands(app):
#    @app.cli.command()
#    @click.option('--username', help="input username")
#    @click.option('--password', help='input password')
#    def inituser(username, password):
#        """Building Bluelog, just for you."""
#        click.echo('Initializing the database...')



if __name__ == '__main__':
    myapp.run(debug=True)


