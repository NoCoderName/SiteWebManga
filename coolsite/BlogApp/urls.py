from django.urls import path

from .views import *


urlpatterns = [
    path('', MangaHome.as_view(), name='home'),
    # path('category/<slug:cat_slug>/', category, name='category'),
    path('about/', About.as_view(), name='about'),
    path('post/<slug:post_slug>/', Showpost.as_view(), name='post'),
]