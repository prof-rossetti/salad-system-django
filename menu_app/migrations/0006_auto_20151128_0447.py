# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0005_auto_20151128_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=8, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=11, decimal_places=8, blank=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
