# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import blanc_basic_pages.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.", unique=True, max_length=100, verbose_name='URL', validators=[django.core.validators.RegexValidator(regex='^[-\\w/\\.~]+$', message='This value must contain only letters, numbers, dots, underscores, dashes, slashes or tildes.'), blanc_basic_pages.models.slash_validator])),
                ('title', models.CharField(max_length=200)),
                ('show_in_navigation', models.BooleanField(default=True, db_index=True)),
                ('content', models.TextField(blank=True)),
                ('template_name', models.CharField(max_length=100, blank=True)),
                ('published', models.BooleanField(default=True, db_index=True)),
                ('login_required', models.BooleanField(default=False, db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='pages.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
