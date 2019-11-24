# !usr/bin/env/python3
# -*- coding:utf-8 -*-

from flask import Blueprint
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/hello')
def hello():
    return "hello shengyu"


