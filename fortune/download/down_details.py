# -*- coding: UTF-8 -*-
# author: yuanpx

from fortune.utils.details import MinuteDetails
from fortune.utils.eastmoney import EastUtil
from utils.file import FileUtil

dt = EastUtil.stockMap('./Table.txt')


def details(savedir):
    lastDay = EastUtil.lastDay()
    FileUtil.create_dir(savedir)
    dir = FileUtil.path_join(savedir, lastDay)
    subdirs = FileUtil.sub_dirs(savedir)
    if lastDay not in subdirs:
        FileUtil.create_dir(dir)
    for i in range(10):
        files = FileUtil.get_files(dir)
        for code, name in dt.items():
            f1 = FileUtil.path_join(dir, code[2:]) + '.txt'
            if f1 not in files:
                resp = MinuteDetails.do(code[2:])
                FileUtil.write(f1, str(resp))


if __name__ == '__main__':
    try:
        details('MinuteDetails')
    except Exception as e:
        print(e)
