# coding=utf-8

import pymysql

from app import app_config

# TODO pool ?
store = pymysql.connect(
    host=app_config['mysql']['host'],
    user=app_config['mysql']['user'],
    password=app_config['mysql']['pwd'],
    db=app_config['mysql']['db'])

# TODO 封装 execute
