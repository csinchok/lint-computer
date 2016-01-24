# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160123_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='branch',
            field=models.CharField(max_length=255, default='master'),
            preserve_default=False,
        ),
    ]
