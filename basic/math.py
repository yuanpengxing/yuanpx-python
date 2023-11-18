# -*- coding: UTF-8 -*-
import unittest


class MathOperator(unittest.TestCase):

    # 求两个数值的商和余数
    def test_divmod(self):
        print(divmod(5.5, 2))  # 返回两个数值的商和余数

    # 可迭代对象中的元素中的最值
    def test_max(self):
        print(max(1, 2, 3))  # 取最大值
        print(max('1234'))
        print(max(1, 0, -2, key=abs))  # 取绝对值后再比较

        print(min(1, 2, 3))  # 取最小值
        print(min('1234'))
        print(min(1, 0, -2, key=abs))  # 取绝对值后再比较

    # 四舍五入
    def test_round(self):
        print(round(1.3))
        print(round(3.1415926, 4))

    # 可迭代对象中的元素求和
    def test_sum(self):
        print(sum((1.5, 2.5, 3.5, 4.5)))
        print(sum((1, 2, 3, 4), -10))

    # 求绝对值
    def test_abs(self):
        print(abs(-2))
