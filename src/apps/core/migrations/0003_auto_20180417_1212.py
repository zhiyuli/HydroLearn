# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-17 17:12
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180416_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='ref_id',
            field=django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default='', editable=False, help_text='Please enter a unique slug for this Topic (can autogenerate from name field)', max_length=64, populate_from=('ref_id',), unique=True, verbose_name='slug'),
        ),
    ]
