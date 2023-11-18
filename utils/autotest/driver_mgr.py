# -*- coding: UTF-8 -*-
from utils.autotest.driver_data_source import DriverDataSource


class DriverMgr:
    @classmethod
    def screenshot(cls, filename):
        DriverDataSource.get_driver().save_screenshot(filename)

    @classmethod
    def get(cls, url):
        DriverDataSource.get_driver().get(url)