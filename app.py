# coding=utf-8

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if os.environ.get('STOCK_IS_PRO'):
    app.config.from_object('config.product.ProductConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
