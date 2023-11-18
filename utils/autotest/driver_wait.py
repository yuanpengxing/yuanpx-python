# -*- coding: UTF-8 -*-
# author： xing

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from utils.autotest.driver_data_source import DriverDataSource

WAIT_TIME = 10


class WaitElementBy:

    @classmethod
    def class_name(cls, locator):
        e = WebDriverWait(DriverDataSource.get_driver(), WAIT_TIME).until(
            EC.presence_of_element_located((By.CLASS_NAME, locator))
        )
        return e

    @classmethod
    def id(cls, locator):
        e = WebDriverWait(DriverDataSource.get_driver(), WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, locator))
        )
        return e

    @classmethod
    def xpath(cls, locator):
        e = WebDriverWait(DriverDataSource.get_driver(), WAIT_TIME, poll_frequency=0.05).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return e

    @classmethod
    def tag_name(cls, locator):
        e = WebDriverWait(DriverDataSource.get_driver(), WAIT_TIME).until(
            EC.presence_of_element_located((By.TAG_NAME, locator))
        )
        return e


class WaitElementsBy:
    @classmethod
    def xpath(cls, locator):
        e = WebDriverWait(DriverDataSource.get_driver(), WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.XPATH, locator))
        )
        return e
