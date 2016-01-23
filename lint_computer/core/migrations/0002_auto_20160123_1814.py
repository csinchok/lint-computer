# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
                ('line', models.IntegerField()),
                ('column', models.IntegerField()),
                ('severity', models.IntegerField(choices=[(0, 'Error'), (1, 'Warning')], default=0)),
                ('message', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=20, blank=True, null=True)),
                ('reporter', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='error',
            name='report',
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 23, 18, 14, 33, 277814, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='repository',
            field=models.ForeignKey(related_name='reports', to='core.Repository'),
        ),
        migrations.DeleteModel(
            name='Error',
        ),
        migrations.AddField(
            model_name='issue',
            name='report',
            field=models.ForeignKey(related_name='issues', to='core.Report'),
        ),
    ]
