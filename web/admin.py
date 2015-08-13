# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Slider, Category


@admin.register(Slider)
class SliderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
