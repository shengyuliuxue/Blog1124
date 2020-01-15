# !usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template
from flask_login import current_user, login_user
from blog.form import LoginForm

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/hello')
def hello():
    return "hello shengyu"

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)




