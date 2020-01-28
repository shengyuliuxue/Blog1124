# !usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user
from blog.form import LoginForm
from blog.models import User

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/hello')
def hello():
    return "hello shengyu"

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.name.data
        password = form.password.data
        nowuser = User.query.filter_by(username=username).first_or_404(
            description='There is no data with {}'.format(username))
        if nowuser:
            if nowuser.validate_password(password):
                flash('login success')
                login_user(nowuser) #登入用户
                return redirect('https://www.baidu.com/')
        else:
            flash('invalid username or password.', 'warning')
    return render_template('login.html', form=form)




