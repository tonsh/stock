# coding=utf-8

import datetime
import os
import sys
sys.path.append(os.path.abspath('__file__' + '/..'))

import urllib2
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from models.stock import Stock


def run():
    req = urllib2.Request('ftp://115.29.204.48/webdata/ashare_perf.txt')
    response = urllib2.urlopen(req)

    for line in response:
        if not line or '|' not in line:
            continue
        line = map(lambda x: x.strip(), line.split('|'))
        if not line[1]:
            continue

        try:
            stock = Stock(
                code=line[1],
                date=datetime.datetime.strptime(line[0], '%Y%m%d'),
                open=float(line[2] or 0),
                close=float(line[5] or 0),
                high=float(line[3] or 0),
                low=float(line[4] or 0),
                change=float(line[6] or 0),
                change_rate=float(line[7] or 0),
                volume=int(line[8] or 0),
                turnover=int(line[9] or 0),
                market_cap=line[10],
                cons_num=line[11],
                p_e1=line[12],
                p_e2=line[13],
                d_p1=line[14],
                d_p2=line[15],
                open_interest=line[16] or 0,
                settlement_turnover=line[17] or 0,
                modified_duration=line[18] or 0,
                convexity=line[19] or 0,
                yield_to_maturity=line[20] or 0,
                duration=line[21] or 0,
                average_price=line[22] or 0,
                net_price=line[23] or 0,
                interest_reinvestment_price=line[24] or 0,
                reserve=line[25] or 0,
                created_at=datetime.datetime.now()
            )
        except ValueError:
            print line
            raise

        try:
            stock.save()
        except (IntegrityError, InvalidRequestError):
            continue


if __name__ == '__main__':
    run()
