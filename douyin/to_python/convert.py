# -*- coding: UTF-8 -*-
# author: yuanpx

import os

from utils.curlconvert import CurlConvert
from utils.file import FileUtil


def create_py(cURLBase, pysave):
    copy = FileUtil.get_text(cURLBase)
    converter = CurlConvert.to_python(copy)
    CurlConvert.to_script(pysave, converter)


def create_runner(savedir, scriptname, content):
    script1 = scriptname.replace('a.py', 'b.py')
    text = FileUtil.get_text('..\CopyAscURLBase\用户列表获取模板.txt')
    text = text.replace('scriptname', scriptname[:-3])
    text = text.replace('Hello World', content)
    save = os.path.join(savedir, script1)
    with open(save, 'w', encoding='utf-8') as wf:
        wf.write(text)


def user_list():
    files = FileUtil.get_files('..\CopyAscURLBase\用户列表')
    for file in files:
        scriptname = os.path.basename(file)[:9] + '_a.py'
        savedir = './videos_author/'
        save = os.path.join(savedir, scriptname)
        create_py(file, save)
        commit = '比我主页的视美女稍微略差一点，不过老师的身材也是炸裂'
        create_runner(savedir, scriptname, commit)


def user_runner(cURLBash, comment):
    # 单个生成py文件
    userdir = '../CopyAscURLBase/用户列表/'
    scriptname = os.path.basename(userdir + cURLBash)[:9] + '_a.py'
    savedir = './videos_author/'
    save = os.path.join(savedir, scriptname)
    create_py(userdir + cURLBash, save)
    create_runner(savedir, scriptname, comment)


if __name__ == '__main__':
    # create_py('..\CopyAscURLBase\发表评论.txt', 'publish.py')
    # user_list()
    user_runner('Author002_咩咩阿银呀.txt', '比我主页的美女稍微略差一些，不过老师的身材也是炸裂')
    pass
