# -*- coding: UTF-8 -*-
# author: yuanpx
# 下载股票K线图，secid=1.000001: 表示上证指数

import json

import requests


def do(secid, klt='101'):
    url = 'http://push2his.eastmoney.com/api/qt/stock/kline/get'
    params = {
        "cb": "kline_dailys",  # 该参数可随意
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": klt,  # 101表示日线，102表示周线，103表示月线
        "fqt": "1",  # 0表示不复权，1表示前复权，2表示后复权
        "beg": "0",
        "end": "20500000",  # 下载从发行日到现在的所有日线图
        "secid": secid
    }
    resp = json.loads(requests.get(url, data=params).text[13:-2])
    data = resp['data']
    return data


if __name__ == '__main__':
    print(do('1.000001'))
