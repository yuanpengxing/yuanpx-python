# -*- coding: UTF-8 -*-
# author: yuanpx
import importlib
import json
import os

from douyin.to_python import convert
from douyin.to_python.convert import createpy_a, rootpath
from utils.file import FileUtil


def createpy_b(py_a, content):
    text = FileUtil.get_text(convert.rootpath + '/douyin/CopyAscURLBase/用户列表获取模板.txt')
    text = text.replace('Script Name', os.path.basename(py_a)[:-3])
    text = text.replace('Hello World', content)
    save = os.path.join(py_a.replace('a.py', 'b.py'))
    with open(save, 'w', encoding='utf-8') as wf:
        wf.write(text)


def create_batch():
    files = FileUtil.get_files(rootpath + '/douyin/CopyAscURLBase/AuthorList/')
    for file in files:
        scriptname = os.path.basename(file)[:9] + '_a.py'
        savedir = rootpath + '/douyin/to_python/author_list/'
        py_a = os.path.join(savedir, scriptname)
        createpy_a(file, py_a)
        commit = '比我主页的视频美女稍微略差一些，不过老师的身材也是炸裂'
        createpy_b(py_a, commit)


def create_single(cURLBash, comment):
    # 单个生成py文件
    userdir = rootpath + '/douyin/CopyAscURLBase/AuthorList/'
    savedir = rootpath + '/douyin/to_python/author_list/'
    scriptname = os.path.basename(cURLBash)[:9] + '_a.py'
    py_a = os.path.join(savedir, scriptname)
    createpy_a(userdir + cURLBash, py_a)
    createpy_b(py_a, comment)


def author_list(script_name):
    # script_name = Author001_a
    module = importlib.import_module('douyin.to_python.author_list.' + script_name)
    method = getattr(module, 'do')
    aweme_list = json.loads(method())['aweme_list']
    aweme_dt = {}
    for aweme in aweme_list:
        aweme_dt[aweme['aweme_id']] = {
            'nickname': aweme['author']['nickname'],
            'desc': aweme['desc'],
            'create_time': aweme['create_time']
        }
    return aweme_dt


if __name__ == '__main__':
    # create_single('Author002_咩咩阿银呀.txt', '比我主页的美女稍微略差一些，不过老师的身材也是炸裂')
    create_batch()
