from time import sleep
from django.apps import apps

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        import mailing.signals
    #     from mailing.jobs import jobs
    #     sleep(2)
    #     jobs.start()

