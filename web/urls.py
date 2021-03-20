from django.conf.urls import url

from .views import HomeView, WhatAreWeView, FavoriteTracksView, UploadTracksView, CategoryView, get_like_ajax_view, \
    like_ajax_view

app_name = 'web'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^nosotros/$', WhatAreWeView.as_view(), name='what'),
    url(r'^favoritos/$', FavoriteTracksView.as_view(), name='favorite'),
    url(r'^subir/$', UploadTracksView.as_view(), name='upload'),
    url(r'^categorias/(?P<slug>.*)/$', CategoryView.as_view(), name='category'),
    url(r'^like/(?P<pod>\d+)/$', get_like_ajax_view, name='like'),
    url(r'^like/plus/(?P<pod>\d+)/$', like_ajax_view, name='like_plus'),

]
