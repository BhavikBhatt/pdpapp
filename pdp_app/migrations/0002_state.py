# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('numpdp', models.IntegerField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]
