# !usr/bin/env/python3
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, session
from ..models import Post
from flask_sqlalchemy import Pagination

blog_bp = Blueprint('blog', __name__)



@blog_bp.route('/post/<int:page>', methods=['GET'])
def show_post(page=1):
    #show the post with the given
    per_page = 10
    pagination = Post.query.order_by(Post.id).paginate(page, per_page, error_out=True)
    posts = pagination.items
    return render_template('posts.html', posts=posts, pagination=pagination)

@blog_bp.route('/')
def index():
    return redirect(url_for('blog.show_post', page=1))


@blog_bp.route('/visit-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Total visits:{x}".format(x=session.get('visits'))

@blog_bp.route('/delete-visits')
def delete_visits():
    session.pop('visits', None)
    return 'visits deleted'

@blog_bp.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item
    return res



