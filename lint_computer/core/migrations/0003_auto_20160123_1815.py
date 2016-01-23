# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160123_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
