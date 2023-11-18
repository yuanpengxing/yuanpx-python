# -*- coding: UTF-8 -*-
# author: yuanpx

def mytry(fun):
    def warpper(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except Exception as e:
            print(e)

    return warpper
