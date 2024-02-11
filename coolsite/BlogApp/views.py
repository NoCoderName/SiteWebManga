from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .utils import *


class MangaHome(DataMixin, ListView):
    model = Manga
    template_name = 'BlogApp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')

        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Manga.objects.filter(is_published=True)
    

class About(DataMixin, ListView):
    model = Manga
    template_name = 'BlogApp/about.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')

        return dict(list(context.items()) + list(c_def.items()))
    

class Showpost(DataMixin, DetailView):
    model = Manga
    template_name = 'BlogApp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))