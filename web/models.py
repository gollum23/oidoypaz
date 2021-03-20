# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from ckeditor.fields import RichTextField
from helpers.slughifi import slughifi


def slider_folder(instance, filename):
    return '{}/{}'.format('slider', filename)


def audio_folder(instance, filename):
    ext = filename.split(".")[-1]
    name = '{}.{}'.format(slughifi(instance.title), ext)
    return '{}/{}'.format('podcast', name)


def fonoteca_folder(instance, filename):
    ext = filename.split(".")[-1]
    name = '{}.{}'.format(slughifi(instance.titulo), ext)
    return '{}/{}'.format('fonoteca', name)


class Slider(models.Model):
    img = models.ImageField(
        verbose_name='Imagen',
        upload_to=slider_folder
    )
    order = models.PositiveSmallIntegerField(
        verbose_name='Orden'
    )

    def __str__(self):
        return '{}'.format(self.img.name)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Categoría'
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name='Slug',
        blank=True
    )
    content = RichTextField(
        verbose_name='Descripción'
    )

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slughifi(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Podcast(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Categoría',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='Título',
        max_length=140
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    audio = models.FileField(
        verbose_name='Audio',
        upload_to=audio_folder
    )
    like = models.SmallIntegerField(
        verbose_name='Me gusta',
        default=0
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'


class SoundLibrary(models.Model):
    artist = models.CharField(
        verbose_name='Artista',
        max_length=200
    )
    album = models.CharField(
        verbose_name='Album',
        max_length=200
    )
    track = models.FileField(
        verbose_name='Audio',
        upload_to=fonoteca_folder
    )
    year = models.CharField(
        verbose_name='Año',
        max_length=4
    )
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100
    )

    def __str__(self):
        return '{}'.format(self.titulo)
