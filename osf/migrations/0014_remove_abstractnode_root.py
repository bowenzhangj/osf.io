# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0013_auto_20161028_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstractnode',
            name='root',
        ),
    ]