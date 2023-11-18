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
        create_runner(savedir, scriptname, 'aaaa')


if __name__ == '__main__':
    # create_py('..\CopyAscURLBase\发表评论.txt', 'publish.py')
    user_list()
    pass
