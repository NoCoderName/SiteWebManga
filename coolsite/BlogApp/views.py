from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .utils import *

from CommentApp.forms import CommentForm


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
    

class Showpost(FormMixin, DataMixin, DetailView):
    model = Manga
    form_class = CommentForm
    template_name = 'BlogApp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.sender = self.request.user
        comment.message = form.cleaned_data['message']
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post', kwargs={'post_slug': self.object.slug})
    