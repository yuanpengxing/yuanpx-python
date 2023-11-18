# -*- coding: UTF-8 -*-
# author: yuanpx

from fortune.utils import klines


class EastUtil:
    @classmethod
    def getSecid(cls, code):
        secid = "1." + code if code.startswith('6') else "0." + code
        return secid

    @classmethod
    def lastDay(cls):
        lines = klines.do('1.000001')['klines']
        return lines[-1][:10]

    @classmethod
    def stockMap(cls, file):
        dt = {}
        with open(file) as rf:
            for line in rf.readlines():
                if line.startswith('S'):
                    split = line.split('\t')
                    code = split[0].strip()
                    name = split[1].strip()
                    dt[code] = name
        return dt


if __name__ == '__main__':
    print(EastUtil.stockMap('C:\\Users\Think\Desktop\Table.txt'))
