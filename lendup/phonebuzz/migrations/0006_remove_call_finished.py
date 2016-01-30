# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebuzz', '0005_call_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='finished',
        ),
    ]
