# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-20 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20190120_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wife',
            options={'verbose_name': '夫人', 'verbose_name_plural': '夫人'},
        ),
        migrations.AddField(
            model_name='wife',
            name='author_set',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Author', verbose_name='作者'),
        ),
    ]