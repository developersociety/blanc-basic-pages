# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blanc_basic_assets.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='hero_image',
            field=blanc_basic_assets.fields.AssetForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Image'),
        ),
    ]
