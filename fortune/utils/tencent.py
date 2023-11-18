# -*- coding: UTF-8 -*-
# author: yuanpx
"""
每日收盘信息下载（腾讯）：http://qt.gtimg.cn/q=sz000858
"""

import datetime
import os

import requests

from fortune.utils.eastmoney import EastUtil


class TencentUtil:
    @classmethod
    def down_curr_data(cls, code):
        # code = SH600001
        url = 'http://qt.gtimg.cn/q=' + code.lower()
        resp = requests.get(url).text
        return resp


if __name__ == '__main__':
    pass
