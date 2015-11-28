# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='location_id',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='menuitemrole',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='menuitemrole',
            old_name='menu_item_id',
            new_name='menu_item',
        ),
    ]
