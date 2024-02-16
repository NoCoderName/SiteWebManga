import django.db
from django.shortcuts import redirect
from django.views.generic import View

from .models import *

from BlogApp.utils import DataMixin


class AddReadManga(DataMixin, View):
    model = Profile

    def get(self, request, *args, **kwargs):
        profile = self.model.objects.get(user=request.user)
        manga = Manga.objects.get(slug=kwargs.get('slug'))
        profile.read.add(manga)
        return redirect('home')