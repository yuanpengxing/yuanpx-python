# -*- coding: UTF-8 -*-

import unittest


class CompileOperator(unittest.TestCase):
    # 将字符串编译为代码或者AST对象，使之能够通过exec或者eval语句来执行
    def test_compile(self):
        # 流程语句使用exec
        str1 = "for i in range(0,10): print(i)"
        c1 = compile(str1, '', 'exec')
        exec(c1)

        # 简单求值表达式用eval
        str2 = "3 * 4 + 5"
        c2 = compile(str2, '', 'eval')
        print(eval(c2))

    # eval：只能执行单个运算表达式（不支持任意形式的赋值操作），不能是复杂的代码逻辑，跟lanbda表达式比较相似
    def test_eval(self):
        print(eval('1+2+3+4'))

    # 动态执行python代码，可以执行复杂的python代码，不像eval函数那样只能计算一个表达式的值
    def test_exec(self):
        b = exec('a=1+2')
        print(b)
