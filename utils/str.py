# -*- coding: UTF-8 -*-
# author: yuanpx


class StringUtil:
    @classmethod
    def str_to_unicode(cls, string):
        s = ''
        for ch in string:
            if '\u4e00' <= ch <= '\u9fff':
                s += hex(ord(ch)).replace('0x', '\\u')
            else:
                s += ch
        return s

    @classmethod
    def rjust(cls, string, length, sep=' '):
        iChineseCharNo = 0
        iEnglishCahrNo = 0
        for char in string:
            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否为中文字符，注意要用utf-8编码
                iChineseCharNo += 1
            else:
                iEnglishCahrNo += 1
        iTotalCharNo = iChineseCharNo * 2 + iEnglishCahrNo
        if iTotalCharNo <= length:
            return sep * (length - iTotalCharNo) + string
        else:
            return string

    @classmethod
    def ljust(cls, string, length, sep=' '):
        iChineseCharNo = 0
        iEnglishCahrNo = 0
        for char in string:
            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否为中文字符，注意要用utf-8编码
                iChineseCharNo += 1
            else:
                iEnglishCahrNo += 1
        iTotalCharNo = iChineseCharNo * 2 + iEnglishCahrNo
        if iTotalCharNo <= length:
            return string + sep * (length - iTotalCharNo)
        else:
            return string

    @classmethod
    def match1(cls, s, boundleft, boundright, right=False):
        # 匹配字符串之间的内容，不包含左边界和右边界
        index1 = s.index(boundleft) + len(boundleft)
        s = s[index1:]
        if right:
            return s[:s.rindex(boundright)]
        else:
            return s[:s.index(boundright)]

    @classmethod
    def match3(cls, str, boundleft, boundright, matchs):
        # 匹配字符串之间的内容，包含左边界和右边界，多次匹配
        index1 = str.index(boundleft) + len(boundleft)
        s1 = str[index1:]
        index2 = s1.index(boundright)
        s2 = s1[:index2]
        s3 = s1[index2:]
        matchs.append(boundleft + s2 + boundright)
        if boundright in s3 and boundleft in s3:
            cls.match3(s3, boundleft, boundright, matchs)
        else:
            pass

    @classmethod
    def match2(cls, str, boundleft, boundright, matchs):
        # 匹配字符串之间的内容，不包含左边界和右边界，多次匹配
        index1 = str.index(boundleft) + len(boundleft)
        s1 = str[index1:]
        index2 = s1.index(boundright)
        s2 = s1[:index2]
        s3 = s1[index2:]
        matchs.append(s2)
        if boundright in s3 and boundleft in s3:
            cls.match2(s3, boundleft, boundright, matchs)
        else:
            pass


if __name__ == '__main__':
    pass
