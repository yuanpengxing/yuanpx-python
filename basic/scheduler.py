# -*- coding: UTF-8 -*-
# author: yuanpx

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import date, datetime
from pytz import timezone

exxcutors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


def work():
    print('work')


scheduler = BlockingScheduler(executors=exxcutors, job_defaults=job_defaults, timezone=timezone('Asia/Shanghai'))
scheduler.add_job(func=work, trigger=CronTrigger(second=30))
scheduler.add_job(work, 'date', run_date=date(2023, 5, 4))
scheduler.add_job(func=work, trigger='date', run_time=datetime(2023, 5, 4, 12, 30, 5))
scheduler.add_job(work, 'date', run_time=datetime(2023, 5, 4, 12, 30, 5))
scheduler.add_job(work, 'interval', minutes=2, start_date='2023-02-04 17:00:00', end_date='2023-02-04 18:00:00')

scheduler.start()
