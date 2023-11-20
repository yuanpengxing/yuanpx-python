# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib
import json
import time


def start():
    py_bs = {
        'Author001_a': {'aweme_ids': [], 'flag': True},
        'Author002_a': {'aweme_ids': [], 'flag': True},
        'Author003_a': {'aweme_ids': [], 'flag': True},
        'Author004_a': {'aweme_ids': [], 'flag': True}
    }
    while True:
        for py_b, value in py_bs.items():
            try:
                module = importlib.import_module(py_b)
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
                if value['flag']:
                    value['aweme_ids'] = list(aweme_dt.keys())
                    value['flag'] = False
                else:
                    set1 = set(list(aweme_dt.keys()))
                    set2 = set(value['aweme_ids'])
                    print(set1)
                    print(set2)
                    diff = set1.difference(set2)
                    if diff:
                        print(diff)
            except Exception as e:
                print(e)
                pass
            time.sleep(2)
        time.sleep(15)


if __name__ == '__main__':
    start()
