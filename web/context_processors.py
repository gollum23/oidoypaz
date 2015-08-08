# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404
from .models import Slider


def slider(request):
    slides = Slider.objects.all()

    return {'slider': slides}
