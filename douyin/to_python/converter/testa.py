# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib

module = importlib.import_module('douyin.to_python.author_list.' + 'Author001_a')
method = getattr(module, 'do')
resp = method()
print(resp)