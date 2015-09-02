# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_soundlibrary_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='like',
            field=models.SmallIntegerField(default=0, verbose_name='Me gusta'),
        ),
    ]
