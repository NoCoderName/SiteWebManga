import django.db
from django.shortcuts import redirect
from django.views.generic import View, DetailView
from django.contrib.auth import get_user_model

from .models import *

from BlogApp.utils import DataMixin


class AddReadManga(DataMixin, View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        profile = self.model.objects.get(user=request.user)
        manga = Manga.objects.get(slug=kwargs.get('slug'))
        profile.read.add(manga)
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