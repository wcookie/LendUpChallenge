# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebuzz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='delay',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='call',
            name='number',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
