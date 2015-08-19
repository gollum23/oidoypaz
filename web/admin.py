# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Slider, Category, Podcast, SoundLibrary


@admin.register(Slider)
class SliderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Podcast)
class PodcastModelAdmin(admin.ModelAdmin):
    pass


@admin.register(SoundLibrary)
class SoundLibraryModelAdmin(admin.ModelAdmin):
    pass
