# !usr/bin/env/python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from ..models import Post
from flask_sqlalchemy import Pagination

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    posts = Post.query.all()[:10]
    print(posts)
    return render_template('base.html', posts=posts)

@blog_bp.route('/post/<int:page>', methods=['GET'])
def show_post(page=1):
    #show the post with the given
    per_page = 10
    pagination = Post.query.order_by(Post.id).paginate(page, per_page, error_out=True)
    posts = pagination.items
    return render_template('posts.html', posts=posts, pagination=pagination)