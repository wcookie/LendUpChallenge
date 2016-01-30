# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebuzz', '0004_call_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='finished',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
