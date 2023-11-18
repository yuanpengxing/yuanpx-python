# -*- coding: UTF-8 -*-
# author: yuanpx

import importlib

module = importlib.import_module('Author001_a')
method = getattr(module, 'do')
print(method())