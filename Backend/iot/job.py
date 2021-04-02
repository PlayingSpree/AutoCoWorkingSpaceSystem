import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.date import DateTrigger
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore


scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()


def iot_on(ip):
    print('Try turning on IoT ip:{}'.format(ip))
    requests.get('http://{}/on'.format(ip))


def iot_off(ip):
    print('Try turning off IoT ip:{}'.format(ip))
    requests.get('http://{}/off'.format(ip))


def add_job_iot_on(room_ip, reserve_id, date):
    return scheduler.add_job(
        iot_on,
        trigger=DateTrigger(run_date=date),
        id="{}on".format(reserve_id),
        max_instances=1,
        replace_existing=True,
        args=[room_ip]
    )


def add_job_iot_off(room_ip, reserve_id, date):
    return scheduler.add_job(
        iot_off,
        trigger=DateTrigger(run_date=date),
        id="{}off".format(reserve_id),
        max_instances=1,
        replace_existing=True,
        args=[room_ip]
    )


def remove_job(job_id):
    scheduler.remove_job(job_id)
