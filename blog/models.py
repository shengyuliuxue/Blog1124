from blog.db import db
from datetime import datetime
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), default='shengyu')
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


