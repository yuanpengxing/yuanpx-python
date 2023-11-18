# -*- coding: UTF-8 -*-
# author: yuanpx

from fortune.utils.eastmoney import EastUtil
from fortune.utils.sdltgd import Sdltgd
from utils.file import FileUtil

dt = EastUtil.stockMap('./Table.txt')


def sdltgd(savedir, date):
    FileUtil.create_dir(savedir)
    dir = FileUtil.path_join(savedir, date)
    subdirs = FileUtil.sub_dirs(savedir)
    if date not in subdirs:
        FileUtil.create_dir(dir)
    for i in range(10):
        files = FileUtil.get_files(dir)
        for code, name in dt.items():
            f1 = FileUtil.path_join(dir, code[2:8]) + '.txt'
            if f1 not in files:
                resp = Sdltgd().do(code, date)
                FileUtil.write(f1, str(resp))


if __name__ == '__main__':
    try:
        sdltgd('Sdltgd', '2023-09-30')
    except Exception as e:
        print(e)
