# !usr/bin/env/python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    return render_template('child.html')

