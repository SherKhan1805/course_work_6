# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# from .task import send_mailing
#
#
# def start():
#     periodicity = send_mailing()
#
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(send_mailing, trigger=CronTrigger.from_crontab(periodicity))
#     scheduler.start()
