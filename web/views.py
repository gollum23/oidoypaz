# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView

from web.models import Category, Podcast


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


def get_like_ajax_view(request, pod):
    if request.is_ajax():
        podcast = Podcast.objects.get(pk=pod)
        data = {'likes': podcast.like}
        return JsonResponse(data, safe=False)


def like_ajax_view(request, pod):
    if request.is_ajax():
        podcast = Podcast.objects.get(pk=pod)
        podcast.like += 1
        podcast.save()
        data = {'likes': podcast.like}
        return JsonResponse(data, safe=False)
