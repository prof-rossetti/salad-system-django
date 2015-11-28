# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_auto_20151128_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(unique=True, max_length=55),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='menuitemrole',
            unique_together=set([('menu', 'menu_item')]),
        ),
        migrations.AlterIndexTogether(
            name='menuitemrole',
            index_together=set([('menu', 'menu_item')]),
        ),
    ]
