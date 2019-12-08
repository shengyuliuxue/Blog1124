# !usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/hello')
def hello():
    return "hello shengyu"


