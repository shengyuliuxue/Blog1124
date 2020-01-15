from blog.db import db
from datetime import datetime
from flask_login import UserMixin
import  blog

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), default='shengyu')
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='post', lazy=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(128))

@blog.login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
