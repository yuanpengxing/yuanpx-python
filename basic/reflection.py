# -*- coding: UTF-8 -*-
import unittest


class Reflection(unittest.TestCase):

    # 检查对象是否含有属性
    def test_hasattr(self):
        o = TestA("zhangsan")
        print(hasattr(o, 'name'))
        print(hasattr(o, 'age'))

    # 获取对象的属性值，如果给的属性不存在则会抛异常，所有要先判断一下该属性是否存在
    def test_getattr(self):
        o = TestA('zhangsan')
        print(getattr(o, 'name'))
        print(getattr(o, 'age'))

    # 设置、添加对象的属性值
    def test_setattr(self):
        o = TestA('zhangsan')
        setattr(o, 'name', 'Bob')
        setattr(o, 'age', '24')
        print(getattr(o, 'name'))
        print(getattr(o, 'age'))

    # 删除对象的属性
    def test_delattr(self):
        o = TestA('zhangsan')
        delattr(o, 'name')
        print(getattr(o, 'name'))


class TestA:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('hello', self.name)
