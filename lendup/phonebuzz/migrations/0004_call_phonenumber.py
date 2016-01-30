# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebuzz', '0003_auto_20160129_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='phoneNumber',
            field=models.CharField(default='+12037278945', max_length=50),
            preserve_default=False,
        ),
    ]
