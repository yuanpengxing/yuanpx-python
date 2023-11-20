# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib
import json
import time

from douyin.to_python import publish
from utils.file import FileUtil


def start():
    flag, aweme_ids = True, []
    while True:
        try:
            module = importlib.import_module('Author004_a')
            method = getattr(module, 'do')
            resp = method()
            aweme_list = json.loads(resp)['aweme_list']
            print(aweme_list[0]['desc'])
            aweme_dt = {}
            for aweme in aweme_list:
                aweme_dt[aweme['aweme_id']] = {
                    'nickname': aweme['author']['nickname'],
                    'desc': aweme['desc'],
                    'create_time': aweme['create_time']
                }
            ids = list(aweme_dt.keys())
            if flag:
                aweme_ids = ids
                flag = False
            else:
                diff = set(ids).difference(set(aweme_ids))
                if diff:
                    aweme_ids = ids
                    id = diff[0]
                    name = aweme_dt[id]['nickname']
                    desc = aweme_dt[id]['desc']
                    FileUtil.append('log.txt', '%s, %s, ' % (name, desc))
                    publish.data['aweme_id'] = id
                    publish.data['text'] = '比我主页的视频美女稍微略差一些，不过老师的身材也是炸裂'
                    resp = publish.do()
                    FileUtil.append('log.txt', resp + '\n')
        except Exception as e:
            print(e)
            pass
        time.sleep(10)


if __name__ == '__main__':
    start()
