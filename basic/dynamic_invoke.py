# -*- coding: UTF-8 -*-

import importlib


# 根据路径（从项目根目录开始，如：dynamic_invoke.lib.module），动态获取到某个py模块
module = importlib.import_module('dynamic_invoke.lib.module')

# 获取模块方法：根据 模块 + 方法名，即可获取模块方法名，执行接收返回值
# module.dynamic()
module_method_obj = getattr(module, 'dynamic')
result = module_method_obj()
print(result)


# 获取类方法：先获得类（模块 + 类名），再根据 类名 + 方法名 获得方法，然后即可进行相应的操作
# 先获得类
module_class = getattr(module, 'ClassA')
class_obj = module_class()
# print(class_obj)
# class_obj.test()

# 根据类获得方法
method_obj = getattr(class_obj, 'test')
method_obj()