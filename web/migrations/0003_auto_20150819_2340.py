# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import web.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, verbose_name='T\xedtulo')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('audio', models.FileField(upload_to=web.models.audio_folder, verbose_name='Audio')),
            ],
            options={
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcasts',
            },
        ),
        migrations.CreateModel(
            name='SoundLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=200, verbose_name='Artista')),
                ('album', models.CharField(max_length=200, verbose_name='Album')),
                ('track', models.FileField(upload_to=web.models.fonoteca_folder, verbose_name='Audio')),
                ('year', models.CharField(max_length=4, verbose_name='A\xf1o')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Categor\xeda', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='category',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Categor\xeda'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', to='web.Category', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
