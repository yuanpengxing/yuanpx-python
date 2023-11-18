# -*- coding: UTF-8 -*-
# author: yuanpx

def test_dict_merge():
    # 测试多个字典合并成一个字典
    d1 = {'a': [1], 'c': 2}
    d2 = {'a': 2, 'b': 2}
    d3 = {'a': [4], 'b': 2}

    d4 = {**d1, **d2, **d3}  # 如果key相同，value保留最后传进的字典的value
    print(d4)


# test_dict_merge()


def test_dict_loops():
    # 字典迭代方式之一，推荐
    d1 = {'a': [1], 'c': 2, 'd': 'HAHA'}
    for key, value in d1.items():
        print(key + ': ' + str(value))


# test_dict_loops()

def dict_find_same(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    same_set = set1 & set2
    return same_set


def dict_find_diff(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    same_set = set1 & set2
    return (set1 - same_set, set2 - same_set)


