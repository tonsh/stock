# coding=utf-8

import datetime

from app import db


class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6))
    name = db.Column(db.String)
    date = db.Column(db.Date)
    open = db.Column(db.Float)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    change = db.Column(db.Float)
    change_rate = db.Column(db.Float)
    volume = db.Column(db.BigInteger)
    turnover = db.Column(db.BigInteger)
    market_cap = db.Column(db.Integer)
    cons_num = db.Column(db.Integer)
    p_e1 = db.Column(db.Float)
    p_e2 = db.Column(db.Float)
    d_p1 = db.Column(db.Float)
    d_p2 = db.Column(db.Float)
    open_interest = db.Column(db.Integer)
    settlement_turnover = db.Column(db.Integer)
    modified_duration = db.Column(db.Integer)
    convexity = db.Column(db.Integer)
    yield_to_maturity = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    average_price = db.Column(db.Integer)
    net_price = db.Column(db.Integer)
    interest_reinvestment_price = db.Column(db.Integer)
    reserve = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    #def __init__(self, code, date, **kwargs):
    #    self.code = code
    #    self.date = date

    #    keys = ['change_rate', 'volume', 'turnover', 'market_cap', 'cons_num',
    #            'p_e1', 'p_e2', 'd_p1', 'd_p2', 'open_interest',
    #            'settlement_turnover', 'modified_duration', 'convexity',
    #            'yield_to_maturity', 'duration', 'average_price', 'net_price',
    #            'interest_reinvestment_price', 'reserve', 'created_at']
    #    for key in keys:
    #        if key in kwargs:
    #            setattr(self, key, kwargs[key])

    def __repr__(self):
        return '<Stock %s - %s>' % (self.code, self.name)

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        if not self.created_at:
            self.created_at = datetime.datetime.now()

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
