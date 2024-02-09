from django.urls import path, re_path
from django.contrib.auth import get_user_model

from .views import *


urlpatterns = [
    path('', MangaHome.as_view(), name='home'),
    path('category/<slug:cat_slug>/', category, name='category'),
    path('about/', About.as_view(), name='about'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', Showpost.as_view(), name='post'),
    path('chat/', MessageUser.as_view(), name='chat'),
    # path('add/<slug:post_slug>/', get_user_model, name='add')
]