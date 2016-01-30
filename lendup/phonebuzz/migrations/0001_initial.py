# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sid', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True)),
                ('delay', models.CharField(blank=True, max_length=50)),
                ('number', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
