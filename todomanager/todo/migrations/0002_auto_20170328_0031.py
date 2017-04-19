# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 29, 0, 31, 15, 625306, tzinfo=utc), null=True),
        ),
    ]
