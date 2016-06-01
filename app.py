# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stock_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
