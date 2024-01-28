# Generated by Django 5.0.1 on 2024-01-24 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('surname', models.CharField(max_length=50, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=50, verbose_name='название компании')),
                ('address', models.CharField(max_length=50, verbose_name='адрес компании')),
                ('phone', models.CharField(max_length=35, verbose_name='телефон')),
                ('email_company', models.EmailField(max_length=254, unique=True, verbose_name='почта компании')),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'партнер',
                'verbose_name_plural': 'партнер',
                'ordering': ('name_company',),
            },
        ),
        migrations.CreateModel(
            name='ClientsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название списка')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='клиент для списка')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.partner')),
            ],
            options={
                'verbose_name': 'список клиентов для рассылки',
                'verbose_name_plural': 'список клиентов для рассылки',
                'ordering': ('name',),
            },
        ),
    ]
