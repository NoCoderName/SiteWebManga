from django.urls import path

from .views import *

urlpatterns = [
    path('add/<slug:slug>/', AddReadManga.as_view(), name='add'),
]