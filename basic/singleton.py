# -*- coding: UTF-8 -*-


# 方式一：Python模块就是天然的单例模式，因为python模块只会加载一次
class Singleton01:
    def __init__(self):
        pass


s = Singleton01()


# 方式二：使用装饰器，实现原理：创建一个字典用来保存类的实例对象，然后每次创建对象的时候,都去这个字典中判断一下是否存在
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        return _instance[cls]

    return _singleton


@singleton
class TestA(object):
    def __init__(self, x=0):
        self.x = x
        print('这是A的类的初始化方法')


a1 = TestA(2)
a2 = TestA(3)
print(a1)
print(a2)

# 方式三：基于__new__方法实现的单例模式(推荐)， 一个对象的实例化过程是先执行类的__new__方法,默认调用object的__new__方法,
# 返回一个实例化对象,然后再调用__init__方法
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                # cls._instance = super().__new__(cls)
                Singleton._instance = object.__new__(cls) # 同上

        return cls._instance


o1 = Singleton()
o2 = Singleton()
print(o1)
print(o2)
