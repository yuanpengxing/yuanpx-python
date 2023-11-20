# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib
import json
import time

from douyin.to_python import publish
from utils.file import FileUtil
from utils.time import TimeUtil

py_bs = ['Author001_a', 'Author002_a', 'Author003_a', 'Author004_a']


def start():
    while True:
        for py_b in py_bs:
            try:
                module = importlib.import_module(py_b)
                method = getattr(module, 'do')
                resp = method()
                aweme_list = json.loads(resp)['aweme_list']
                print(aweme_list[0]['desc'])
                timestamp = time.time()
                for aweme in aweme_list:
                    nickname = aweme['author']['nickname']
                    create_time = aweme['create_time']
                    aweme_id = aweme['aweme_id']
                    desc = aweme['desc']
                    if (timestamp - float(create_time)) < 20:
                        dt = TimeUtil.getTimeFormat2(timestamp)
                        FileUtil.append('log.txt', '%s, %s, %s, ' % (dt, nickname, desc))
                        publish.data['aweme_id'] = aweme_id
                        publish.data['text'] = '比我主页的视频美女稍微略差一些，不过老师的身材也是炸裂'
                        resp = publish.do()
                        FileUtil.append('log.txt', resp + '\n')
                    else:
                        pass
            except Exception as e:
                pass
            time.sleep(2)
        time.sleep(15)


if __name__ == '__main__':
    start()
