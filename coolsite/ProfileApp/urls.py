from django.urls import path

from .views import *

app_name = 'profile_user'

urlpatterns = [
    path('add/<slug:slug>/', AddReadManga.as_view(), name='add'),
    path('profile/<slug:prof_slug>/', ProfileView.as_view(), name='profile'),
]