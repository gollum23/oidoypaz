# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


def slider_folder(instance, filename):
    return '{}/{}'.format('slider', filename)


@python_2_unicode_compatible
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
