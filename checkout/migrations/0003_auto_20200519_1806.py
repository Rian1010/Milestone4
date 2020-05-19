# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-19 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_buyproduct_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='buyproduct',
            name='street_address2',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
