# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Slider


@admin.register(Slider)
class SliderModelAdmin(admin.ModelAdmin):
    pass
