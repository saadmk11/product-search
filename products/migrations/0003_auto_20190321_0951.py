# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190321_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='final_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.IntegerField(),
        ),
    ]