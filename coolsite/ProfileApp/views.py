import django.db
from django.shortcuts import redirect
from django.views.generic import View, DetailView
from django.contrib.auth import get_user_model

from .models import *

from BlogApp.utils import DataMixin


class AddReadManga(DataMixin, View):
    model = get_user_model()
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        manga = Manga.objects.get(slug=kwargs.get('slug'))
        request.user.favorites.add(manga)
        return redirect('home')    


class ProfileView(DataMixin, DetailView):
    model = get_user_model()
    template_name = 'ProfileApp/profile.html'
    context_object_name = 'prof'
    slug_url_kwarg = 'prof_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Профиль')
        return dict(list(context.items()) + list(c_def.items()))