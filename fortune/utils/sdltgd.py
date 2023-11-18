# -*- coding: UTF-8 -*-
# author: yuanpx
import requests


class Sdltgd:
    def do(self, code, date):
        var = (code, date)
        url = 'https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/PageSDLTGD?code=%s&date=%s' % var
        resp = requests.get(url).text
        return resp
