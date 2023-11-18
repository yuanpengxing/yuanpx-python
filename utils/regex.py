# -*- coding: UTF-8 -*-
# author: yuanpx

import re

KuoHao_Xiao = r'[\(](.*?)[)]'
KuoHao_Da = r'[\{](.*?)[}]'
KuoHao_Fang = r'[\[](.*?)[]]'
YinHao_Shuang = r'\"(.*?)\"'
YinHao_Dan = r'\'(.*?)\''


def findShuang(text, pattren=YinHao_Shuang):
    return re.findall(pattren, text)


def findDan(text, pattren=YinHao_Dan):
    return re.findall(pattren, text)


def findXiao(text, pattren=KuoHao_Xiao):
    return re.findall(pattren, text)


def findDa(text, pattren=KuoHao_Da):
    return re.findall(pattren, text)


def findFang(text, pattren=KuoHao_Fang):
    return re.findall(pattren, text)


class RegexUtil:
    tuple1, tuple2, tuple3 = ('(', ')'), ('{', '}'), ('[', ']')

    def _match(self, s, tuple):
        count, end = 0, 0
        for i in range(len(s)):
            char = s[i]
            if tuple[0] == char:
                count += 1
            elif tuple[1] == char:
                count -= 1
                if count == 0:
                    end = i
                    break
        if not count == 0:
            print('格式错误')
        return s[:end + 1]

    def match(self, s):
        char, t = s[0], None
        if char not in ['(', '{', ']']:
            return
        else:
            if char == '(':
                t = self.tuple1
            elif char == '{':
                t = self.tuple2
            elif char == '[':
                t = self.tuple3
            return self._match(s, t)

    def substr(self, s, leftbound):
        s1 = s[s.index(leftbound) + len(leftbound) - 1:]
        if s1[0] not in ['(', '{', ']']:
            return
        else:
            return s1

