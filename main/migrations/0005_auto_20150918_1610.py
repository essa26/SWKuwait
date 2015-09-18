# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='user',
            new_name='userprof',
        ),
    ]
