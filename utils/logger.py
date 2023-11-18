# -*- coding: UTF-8 -*-
# author: yuanpx

import logging
import threading


class LoggerUtils:
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with LoggerUtils._instance_lock:
                cls._instance = super().__new__(cls)
                cls.logger = logging.getLogger()
                formatter = logging.Formatter('%(asctime)s[line:%(lineno)d] %(levelname)s %(message)s')
                fh = logging.FileHandler('test.log', encoding='utf-8')
                ch = logging.StreamHandler()
                fh.setFormatter(formatter)
                ch.setFormatter(formatter)
                fh.setLevel(logging.DEBUG)
                ch.setLevel(logging.DEBUG)
                cls.logger.addHandler(fh)
                cls.logger.addHandler(ch)
        return cls._instance

    def error(cls, error_msg):
        cls.logger.error(error_msg)

    def debug(cls, debug_msg):
        cls.logger.debug(debug_msg)
