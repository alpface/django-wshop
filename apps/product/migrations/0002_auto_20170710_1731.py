# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-10 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品', 'verbose_name_plural': '产品'},
        ),
    ]