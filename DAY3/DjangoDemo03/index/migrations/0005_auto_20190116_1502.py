# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-16 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190116_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
