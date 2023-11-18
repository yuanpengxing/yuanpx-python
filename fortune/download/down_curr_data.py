# -*- coding: UTF-8 -*-
# author: yuanpx

import os

from fortune.utils.eastmoney import EastUtil
from fortune.utils.tencent import TencentUtil
from utils.file import FileUtil

dt = EastUtil.stockMap('./Table.txt')


def curr_data(savedir):
    lastDay = EastUtil.lastDay()
    FileUtil.create_dir(savedir)
    savefile = savedir + '/%s.txt' % lastDay
    if not os.path.exists(savefile):
        with open(savefile, 'w') as wf:
            for code, name in dt.items():
                r = TencentUtil.down_curr_data(code)
                wf.write(r + '\n')


if __name__ == '__main__':
    curr_data('CurrentData')
