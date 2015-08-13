# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Categor\xc3\xada')),
                ('slug', models.SlugField(max_length=100, verbose_name=b'Slug', blank=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'Descripci\xc3\xb3n')),
            ],
        ),
    ]
