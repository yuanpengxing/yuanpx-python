# -*- coding: UTF-8 -*-
# author: yuanpx

import pynput



def on_click(x, y, button, pressed):
    if pressed:
        print(x, y)


def on_press(key):
    print(key)


# 以非阻塞的方式启动鼠标监控
mouse_listener = pynput.mouse.Listener(on_click=on_click)
mouse_listener.start()

# 最后一个监听器以阻塞方式启动
with pynput.keyboard.Listener(on_press=on_press) as keybord_listener:
    keybord_listener.join()
