# !usr/bin/env/python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from ..models import Post

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    posts = Post.query.all()[:10]
    print(posts)
    return render_template('base.html', posts=posts)

