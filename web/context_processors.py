# -*- coding: utf-8 -*-
from .models import Slider, Category


def slider(request):
    slides = Slider.objects.all()

    return {'slider': slides}


def category(request):
    categories = Category.objects.all()

    return {'category_menu': categories}
