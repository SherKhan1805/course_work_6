from django.contrib import admin

from mailing.models import Client, Partner, ClientsList, Mailing, Message, LogMailing

admin.site.register(Client)

admin.site.register(Partner)

admin.site.register(ClientsList)

admin.site.register(Mailing)

admin.site.register(Message)

admin.site.register(LogMailing)
