# -*- coding: UTF-8 -*-
# author: yuanpx
# 下载更多分时成交

import json

import requests

from fortune.utils.eastmoney import EastUtil


class MinuteDetails:
    @classmethod
    def do(cls, code):
        secid = EastUtil.getSecid(code)
        url = 'https://86.push2.eastmoney.com/api/qt/stock/details/sse?fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54,f55&mpi=2000&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&pos=-0&secid=%s&wbp2u=|0|0|0|web' % secid
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            for line in response.iter_lines():
                res = json.loads(line[6:])
                return res['data']


if __name__ == '__main__':
    print(MinuteDetails.do('600328'))
