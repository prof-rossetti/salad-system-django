# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_auto_20151128_0303'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='location',
            table='locations',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menus',
        ),
        migrations.AlterModelTable(
            name='menuitemrole',
            table='menu_item_roles',
        ),
    ]
