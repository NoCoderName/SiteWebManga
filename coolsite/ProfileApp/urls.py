from django.urls import path

from .views import *

app_name = 'profile_user'

urlpatterns = [
    path('add_favorites/<slug:slug>/', AddFavoritesManga.as_view(), name='add_favorites'),
    path('profile/<slug:prof_slug>/', ProfileView.as_view(), name='profile'),
]