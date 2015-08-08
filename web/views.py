# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class WhatAreWeView(TemplateView):
    template_name = 'what_are_we.html'
