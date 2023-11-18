# -*- coding: UTF-8 -*-
# author: yuanpx

import pyautogui

# 默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
pyautogui.FAILSAFE = True

# 意味着所有pyautogui的指令都要暂停一秒；其他指令不会停顿；这样做，可以防止键盘鼠标操作太快；
pyautogui.PAUSE = 0.001

width, height = pyautogui.size() # 屏幕的宽度和高度
print(width, height)
