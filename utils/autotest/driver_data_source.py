# -*- coding: UTF-8 -*-
# author： yuanpx

import threading

from utils.autotest.driver_init_chrome import ChromeInit


class DriverDataSource:
    thread_local = threading.local()

    @classmethod
    def get_driver(cls):
        thread_name = threading.current_thread().getName()
        driver = getattr(cls.thread_local, thread_name, None)
        if driver is None:
            setattr(cls.thread_local, thread_name, ChromeInit.init())
        return getattr(cls.thread_local, thread_name, None)

    @classmethod
    def delete_driver(cls):
        thread_name = threading.current_thread().getName()
        driver = getattr(cls.thread_local, thread_name, None)
        if driver:
            delattr(cls.thread_local, thread_name)
            driver.quit()

    @classmethod
    def new_driver(cls):
        cls.delete_driver()
        driver = ChromeInit.init()
        thread_name = threading.current_thread().getName()
        setattr(cls.thread_local, thread_name, driver)
        return driver
