# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150819_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundlibrary',
            name='titulo',
            field=models.CharField(default='', max_length=100, verbose_name='T\xedtulo'),
            preserve_default=False,
        ),
    ]
