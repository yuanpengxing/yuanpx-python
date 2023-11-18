# -*- coding: UTF-8 -*-
import math
import unittest


class ObjectOperator(unittest.TestCase):
    # 返回对象或者当前作用域内的属性列表
    def test_dir(self):
        print(dir(math))

    # 返回对象的唯一标识符(地址值)
    def test_id(self):
        a = 'hello world'
        print(id(a))

    # 获取对象的哈希值
    def test_hash(self):
        print(hash('hello world'))

    # 返回对象的类型，或者根据传入的参数创建一个新的类型
    def test_type(self):
        print(type('hello world'))

    # 返回可迭代对象的长度
    def test_len(self):
        print(len('abcd'))
        print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
        print(len([1, 2, 3, 4]))

    # 判断对象是否是类或者类型元组中任意类元素的实例
    def test_isinstance(self):
        print(isinstance(1, int))  # True
        print(isinstance(1, str))  # False
        print(isinstance(1, (int, str)))  # True

    # 判断类是否是另外一个类或者类型元组中任意类元素的子类
    def test_issubclass(self):
        print(issubclass(bool, int))  # True
        print(issubclass(bool, str))  # False
        print(issubclass(bool, (str, int)))  # True

    # 检测对象是否可被调用
    def test_callable(self):
        print(callable(ObjectOperator))  # True
        o = ObjectOperator()
        print(callable(o))  # True
