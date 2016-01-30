# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phonebuzz', '0002_auto_20160129_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 18, 50, 59, 961134, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
