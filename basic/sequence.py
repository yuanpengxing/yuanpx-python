# -*- coding: UTF-8 -*-
import unittest


class SequenceOperator(unittest.TestCase):
    # 判断可迭代对象的每个元素是否都为True
    def test_all(self):
        print(all([1, 2]))  # True
        print(all([0, 1, 2]))  # False
        print(all({}))  # True

    # 判断可迭代对象的元素是否有为True值的元素
    def test_any(self):
        print(any([0, 1, 2]))  # True
        print(any({}))  # False
        print(any([]))  # False

    # 使用指定方法过滤可迭代对象的元素
    def test_filter(self):
        a = list(range(1, 10))
        print(list(filter(if_odd, a)))

    # 使用指定方法去作用传入的每个可迭代对象的元素，生成新的可迭代对象
    def test_map(self):
        a = map(ord, 'abcd')
        print(list(a))

    def test_map_iterate(self):
        d = {'a':'1', 'b':'2'}
        for key in d:
            print(d[key])
        for key in d.keys():
            print(key+d[key])
        for kv in d.items():
            print(kv)
        for key,value in d.items():
            print(key+':'+value)

    # 返回可迭代对象中的下一个元素值
    def test_next(self):
        a = iter('abcd')
        print(next(a))

    # 反转序列生成新的可迭代对象
    def test_reversed(self):
        a = reversed(range(10))
        print(list(a))

    # 对可迭代对象进行排序，返回一个新的列表
    def test_sorted(self):
        a = ['a', 'b', 'd', 'c', 'B', 'A']
        print(sorted(a))  # 默认按字符ascii码排序
        print(sorted(a, key=str.lower))  # 转换成小写后再排序


def if_odd(x):  # 定义奇数判断函数
    return x % 2 == 1
