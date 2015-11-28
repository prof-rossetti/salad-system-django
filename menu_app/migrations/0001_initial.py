# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=8)),
                ('longitude', models.DecimalField(max_digits=11, decimal_places=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location_id', models.ForeignKey(to='menu_app.Location')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('calories', models.PositiveIntegerField()),
                ('gluten_free', models.BooleanField()),
                ('vegan_safe', models.BooleanField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'menu_items',
            },
        ),
        migrations.CreateModel(
            name='MenuItemRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=255)),
                ('price_usd', models.DecimalField(max_digits=10, decimal_places=2)),
                ('menu_id', models.ForeignKey(to='menu_app.Menu')),
                ('menu_item_id', models.ForeignKey(to='menu_app.MenuItem')),
            ],
        ),
    ]
