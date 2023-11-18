# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib
import json
import time

from douyin.to_python import publish
from utils.time import TimeUtil


def start():
    while True:
        module = importlib.import_module('scriptname')
        method = getattr(module, 'do')
        resp = method()
        aweme_list = json.loads(resp)['aweme_list']
        timestamp = time.time()
        for aweme in aweme_list:
            create_time = aweme['create_time']
            aweme_id = aweme['aweme_id']
            desc = aweme['desc']
            if (timestamp - float(create_time)) < 20:
                publish.data['aweme_id'] = aweme_id
                publish.data['text'] = 'Hello World'
                print(publish.do())
                print(TimeUtil.getTimeFormat2(timestamp))
                print(desc)
                break
            else:
                pass
        time.sleep(15)


if __name__ == '__main__':
    start()