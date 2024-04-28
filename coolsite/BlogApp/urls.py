from django.urls import path

from .views import *


urlpatterns = [
    path('', MangaHome.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('about/', About.as_view(), name='about'),
    path('post/<slug:post_slug>/', Showpost.as_view(), name='post'),
    path('post_read/<slug:post_slug>/', PostRead.as_view(), name='post_read')
]