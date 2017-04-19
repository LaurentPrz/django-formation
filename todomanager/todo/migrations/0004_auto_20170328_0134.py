# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170328_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 29, 1, 34, 30, 782906, tzinfo=utc), null=True, blank=True),
        ),
    ]
