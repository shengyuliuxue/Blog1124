import click
from faker import Faker
from blog.models import Post, Category, Links
import random
from blog.db import db
from blog import myapp
fake = Faker('zh_CN')


def fake_post(number):
    with myapp.app_context():
        for i in range(number):
            post = Post(
                title=fake.sentence(),
                author=fake.name(),
                pub_date=fake.date_time(),
                content=fake.text(2000),
                category_id=random.randint(1, 10)
            )
            db.session.add(post)
        print(f"init the num {i} post...\n")
        db.session.commit()


def fake_category(catnum):
    with myapp.app_context():
        for i in range(catnum):
            category = Category(
                name=fake.word()
            )
            db.session.add(category)
        db.session.commit()

def fake_links(linknum):
    with myapp.app_context():
        for i in range(linknum):
            link=Links(
                site=fake.domain_name(),
                url=fake.uri()
            )
            db.session.add(link)
        db.session.commit()

