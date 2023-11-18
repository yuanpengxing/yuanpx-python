import sys
import time

import win32com
import win32gui
import win32ui
import win32con
import win32api
from PyQt5.QtWidgets import QApplication

from utils import cmd
from utils.cmd import CmdUtil


def capture_whole_screen(filename):
    hwndDC = win32gui.GetWindowDC(0)  # 0表示当前活跃的窗口
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    # 第4个参数(0, 0)表示截取从左上角(0, 0)开始，截取长宽为(w, h)的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def capture_specify_area(filename, loc1, loc2):
    hwndDC = win32gui.GetWindowDC(0)  # 0表示当前活跃的窗口
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    w = loc2[0] - loc1[0]
    h = loc2[1] - loc1[1]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (loc1[0], loc1[1]), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def mouse_click(locator_tuple):
    win32api.SetCursorPos([locator_tuple[0], locator_tuple[1]])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouse_press(t):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouse_slice(x1, y1, x2, y2):
    win32api.SetCursorPos([x1, y1])  # 鼠标移动到
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # 左键按下
    time.sleep(0.5)
    dx = x2 - x1
    dy = y2 - y1
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouse_wheel(pixel: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1 * pixel)  # 滚动网页


def ctrl_v():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)


def ctrl_a():
    # 组合键输入ctrl+A
    # 注意：先按下的要后抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl按下
    win32api.keybd_event(65, 0, 0, 0)  # a按下
    win32api.keybd_event(65, 0, 0, 0)  # a抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl抬起


def ctrl_q():
    # 组合键输入ctrl+A
    # 注意：先按下的要后抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl按下
    win32api.keybd_event(81, 0, 0, 0)  # a按下
    win32api.keybd_event(81, 0, 0, 0)  # a抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl抬起


def ctrl_c():
    # 组合键输入ctrl+C
    # 注意：先按下的要后抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl按下
    win32api.keybd_event(67, 0, 0, 0)  # c按下
    win32api.keybd_event(67, 0, 0, 0)  # c抬起
    win32api.keybd_event(17, 0, 0, 0)  # ctrl抬起


def delete(times):
    for i in range(times):
        time.sleep(0.15)
        win32api.keybd_event(8, 0, 0, 0)  # 按下
        win32api.keybd_event(8, 0, 0, 0)  # 抬起


def enter():
    win32api.keybd_event(13, 0, 0, 0)  # 按下
    win32api.keybd_event(13, 0, 0, 0)  # 抬起


def esc():
    win32api.keybd_event(27, 0, 0, 0)  # 按下
    win32api.keybd_event(27, 0, 0, 0)  # 抬起


def mouse_move(locator_tuple):
    win32api.SetCursorPos([locator_tuple[0], locator_tuple[1]])


def tab():
    win32api.keybd_event(9, 0, 0, 0)  # 按下
    win32api.keybd_event(9, 0, 0, 0)  # 抬起


def right_arrow():
    win32api.keybd_event(39, 0, 0, 0)  # 按下
    win32api.keybd_event(39, 0, 0, 0)  # 抬起


def left_arrow():
    win32api.keybd_event(37, 0, 0, 0)  # 按下
    win32api.keybd_event(37, 0, 0, 0)  # 抬起


import win32clipboard
from PIL import Image
from io import BytesIO


def copy_image_to_clipboard(img_path: str):
    '''输入文件名，执行后，将图片复制到剪切板'''
    image = Image.open(img_path)
    output = BytesIO()
    image.save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
            win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})


hwnd_map = {}

import win32com.client


def set_app_top(appname: str):
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_map.items():
        if t:
            if t.endswith(appname):
                win32gui.BringWindowToTop(h)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                # 被其他窗口遮挡，调用后放到最前面
                win32gui.SetForegroundWindow(h)
                # 最大化
                win32gui.ShowWindow(h, win32con.SW_MAXIMIZE)
                win32gui.ShowWindow(h, win32con.SW_MAXIMIZE)


def screenshots(savepath):
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(QApplication.desktop().winId())
    img.save(savepath)


def app_top():
    # 关闭桌面现有chrome.exe
    CmdUtil.run_cmd('TASKKILL /F /IM chrome.exe /T')
    # 打开chrome.exe
    win32api.ShellExecute(0, 'open', R'C:\Users\Think\AppData\Local\Google\Chrome\Application\chrome.exe', '', '', 1)
    # 确保chrome为桌面当前应用
    set_app_top('Google Chrome')
