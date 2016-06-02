# coding=utf-8

import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app_config = yaml.load(file(app.root_path + '/app.yaml', 'r'))

app.DEBUG = app_config['debug']
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        app_config['mysql']['user'], app_config['mysql']['pwd'],
        app_config['mysql']['host'], app_config['mysql']['port'],
        app_config['mysql']['db']),
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
})

db = SQLAlchemy(app)
