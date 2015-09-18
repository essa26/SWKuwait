# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='email',
            field=models.CharField(default=datetime.datetime(2015, 9, 18, 12, 55, 37, 49253, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
