# -*- coding: UTF-8 -*-
# author: yuanpx

import json
import time

from douyin.to_python import publish
from douyin.to_python.videos_author import py001


def start():
    while True:
        aweme_list = json.loads(py001.do())['aweme_list']
        timestamp = time.time()
        for aweme in aweme_list:
            create_time = aweme['create_time']
            aweme_id = aweme['aweme_id']
            desc = aweme['desc']
            if (timestamp - float(create_time)) < 2 * 60:
                publish.data['aweme_id'] = aweme_id
                publish.data['text'] = '我主页里的才是真极品，视频里的还略差一点!'
                print(publish.do())
            else:
                print(desc)
        time.sleep(15)


start()
