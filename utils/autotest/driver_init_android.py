# -*-coding:utf-8-*
from appium import webdriver


class AndroidDriverInit:
    @classmethod
    def init(cls):
        desired_caps = {
            "deviceName": "127.0.0.1:62001",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.qyer.android.jinnang",
            "appActivity": "com.qyer.android.jinnang.activity.main.MainActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
        }
        # 声明我们的driver对象
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
