# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=200)),
                ('link', models.CharField(db_column='link', max_length=256)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
