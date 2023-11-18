# -*- coding: UTF-8 -*-

import unittest

# 定义在class、def外的是全局变量
out = 'out'


class VariableOperator(unittest.TestCase):
    # 在class里面，定义全局变量需要global关键字先申明，让程序知道该变量是全局变量，否则当普通变量处理
    global inglobal
    inglobal = 'inglobal'

    # 普通变量，没被申明
    inclass = 'inclass'

    # 返回当前作用域内的全局变量和其值组成的字典
    def test_globals(self):
        print(globals())

    # 返回当前作用域内的局部变量和其值组成的字典
    def test_local(self):
        print(locals())
