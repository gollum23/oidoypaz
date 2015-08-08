# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=web.models.slider_folder, verbose_name=b'Imagen')),
                ('order', models.PositiveSmallIntegerField(verbose_name=b'Orden')),
            ],
        ),
    ]
