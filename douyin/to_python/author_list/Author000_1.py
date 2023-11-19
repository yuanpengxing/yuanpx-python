# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib
import json
import time

from douyin.to_python import publish
from utils.file import FileUtil
from utils.time import TimeUtil

py_as = ['Author001_a', 'Author002_a', 'Author003_a', 'Author004_a']


def start():
    while True:
        for py_a in py_as:
            try:
                module = importlib.import_module(py_a)
                method = getattr(module, 'do')
                resp = method()
                aweme_list = json.loads(resp)['aweme_list']
                timestamp = time.time()
                print(aweme_list[0]['desc'])
                for aweme in aweme_list:
                    create_time = aweme['create_time']
                    aweme_id = aweme['aweme_id']
                    desc = aweme['desc']
                    if (timestamp - float(create_time)) < 30:
                        publish.data['aweme_id'] = aweme_id
                        publish.data['text'] = '比我主页的美女稍微略差一些，不过老师的身材也是炸裂'
                        dt = TimeUtil.getTimeFormat2(timestamp)
                        rsp = publish.do()
                        s = '%s, %s, %s\n' % (dt, desc, rsp)
                        FileUtil.append('log.txt', s)
                    else:
                        pass
                time.sleep(2)
            except Exception as e:
                pass
        time.sleep(20)


if __name__ == '__main__':
    start()
