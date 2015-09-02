# -*- coding: utf-8 -*-
"""oidoypaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from .views import HomeView, WhatAreWeView, FavoriteTracksView, UploadTracksView, CategoryView, get_like_ajax_view, \
    like_ajax_view

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^nosotros/$', WhatAreWeView.as_view(), name='what'),
    url(r'^favoritos/$', FavoriteTracksView.as_view(), name='favorite'),
    url(r'^subir/$', UploadTracksView.as_view(), name='upload'),
    url(r'^categorias/(?P<slug>.*)/$', CategoryView.as_view(), name='category'),
    url(r'^like/(?P<pod>\d+)/$', get_like_ajax_view, name='like'),
    url(r'^like/plus/(?P<pod>\d+)/$', like_ajax_view, name='like_plus'),

]
