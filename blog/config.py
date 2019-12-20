import os.path

class Config(object):
    rootpath = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(rootpath, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False