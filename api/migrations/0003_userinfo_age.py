# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170302_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
