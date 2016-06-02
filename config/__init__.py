# coding=utf-8


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/stock_db'
