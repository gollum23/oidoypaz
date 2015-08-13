# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView

from web.models import Category


class HomeView(TemplateView):
    template_name = 'home.html'


class WhatAreWeView(TemplateView):
    template_name = 'what_are_we.html'


class FavoriteTracksView(TemplateView):
    template_name = 'favorite_tracks.html'


class UploadTracksView(TemplateView):
    template_name = 'upload_tracks.html'


class CategoryView(DetailView):
    template_name = 'detail_category.html'
    model = Category
