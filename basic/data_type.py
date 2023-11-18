# -*- coding: UTF-8 -*-
import unittest


class DataType(unittest.TestCase):

    def test_boolean(self):
        print(bool())  # 初始化默认为False
        print(bool(0))  # 数值0、空序列等值为False
        print(bool(1))  # True

    def test_int(self):
        print(int())  # 初始化默认为0
        print(int('1'))  # str -> int
        print(int(3.6))  # 只保留整数部分

    def test_float(self):
        print(float())  # 初始化默认为0.0
        print(float('3'))  # 3.0
        print(float(3))  # 3.0

    def test_str(self):
        print(str())  # 初始化默认为''
        print(str(123))  # int -> str

    def test_bytes(self):
        print(bytearray('中文', 'utf-8'))  # str -> 字节数组
        print(bytes('中文', 'utf-8'))  # str -> 字节数组

    def test_jinzhi(self):
        print(ord('a'))  # 返回Unicode字符对应的整数
        print(chr(97))  # 返回整数对应的Unicode字符
        print(bin(3))  # 10进制 -> 2进制
        print(oct(10))  # 10进制 -> 8进制
        print(hex(15))  # 10进制 -> 16进制

    def test_tuple(self):
        print(tuple())  # 初始化空元组()
        print(tuple('121'))  # 传入可迭代对象，结果('1', '2', '1')

    def test_list(self):
        print(list())  # 初始化创建空列表[]
        print(list('abcd'))  # 传入可迭代对象，结果['a', 'b', 'c', 'd']

    def test_dict(self):
        print(dict())  # 初始化创建空字典{}
        print(dict(a=1, b=2))  # {'b': 2, 'a': 1}
        print(dict(zip(['a', 'b'], [1, 2])))  # {'a': 1, 'b': 2}

    def test_set(self):
        print(set())  # 初始化创建空set()
        print(set('abcd'))

    def test_iter(self):
        iters = iter('abcd')  # 可迭代对象生成器
        for i in iters:
            print(i)
