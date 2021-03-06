# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=1000)),
                ('line', models.IntegerField()),
                ('column', models.IntegerField()),
                ('severity', models.IntegerField(choices=[(0, 'Error'), (1, 'Warning')], default=0)),
                ('message', models.CharField(max_length=1000)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('reporter', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GithubOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('commit', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
                ('organization', models.ForeignKey(to='core.GithubOrganization', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('username', models.CharField(max_length=100)),
                ('github_id', models.IntegerField(blank=True, null=True)),
                ('github_access_token', models.CharField(blank=True, max_length=45, null=True)),
                ('github_organization', models.ForeignKey(to='core.GithubOrganization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(to='core.User', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='repository',
            field=models.ForeignKey(to='core.Repository'),
        ),
        migrations.AddField(
            model_name='error',
            name='report',
            field=models.ForeignKey(to='core.Report'),
        ),
    ]
