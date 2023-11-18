# -*- coding: UTF-8 -*-
# author: yuanpx

import time
from datetime import datetime, timedelta

FORMAT = '%Y-%m-%d %H:%M:%S'


class TimeUtil:
    @classmethod
    def getTimeStamp1(cls, timestr, format=FORMAT):
        return datetime.timestamp(datetime.strptime(timestr, format))

    @classmethod
    def getTimeStamp2(cls, timedate=None):
        if not timedate:
            timedate = datetime.now()
        return datetime.timestamp(timedate)

    @classmethod
    def getTimeFormat1(cls, timedate=None, days=0, hours=0, minutes=0, seconds=0, format=FORMAT):
        if not timedate:
            timedate = datetime.now()
        t = (timedate + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds))
        return t.strftime(format)

    @classmethod
    def getTimeFormat2(cls, timestamp, format=FORMAT):
        return time.strftime(format, time.localtime(timestamp))

    @classmethod
    def getDateTime1(cls, timestr, format=FORMAT):
        return datetime.strptime(timestr, format)

    @classmethod
    def getDateTime2(cls, timestamp):
        return time.localtime(timestamp)
