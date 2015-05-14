# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('user_starred', models.BooleanField(default=False)),
                ('sessions', models.IntegerField(default=0)),
                ('last_session', models.DateTimeField(null=True, verbose_name=b'Most Recent Session')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('user_goal', models.BooleanField(default=False)),
                ('option_type', models.IntegerField(default=1)),
                ('activity', models.ForeignKey(to='freetime.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=255)),
                ('created_date', models.DateTimeField(verbose_name=b'Date Created')),
                ('last_active', models.DateTimeField(verbose_name=b'Last Active')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rid', models.CharField(unique=True, max_length=255)),
                ('date', models.DateTimeField(verbose_name=b'Activity Date')),
                ('personal_best', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(to='freetime.Activity')),
                ('user_profile', models.ForeignKey(to='freetime.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='categories',
            field=models.ManyToManyField(to='freetime.Category'),
        ),
    ]
