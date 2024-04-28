from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from .models import Manga, Category
from .utils import DataMixin
from .forms import CommentForm


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


class PostRead(DataMixin, DetailView):
    model = Manga
    queryset = Manga.objects.only('manga')
    template_name = 'BlogApp/post_read.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        manga = self.model.objects.get(slug=kwargs.get('post_slug'))
        request.user.read.add(manga)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))


class CatalogView(DataMixin, ListView):
    model = Manga
    context_object_name = 'post'
    template_name = 'BlogApp/catalog.html'
    
    def get_queryset(self):  
        sort_by = self.request.GET.get('sort', '')

        if sort_by == 'rating':
           return self.sort_query(self.request.GET, 'rating')
        elif sort_by == 'years_of_release':
           return self.sort_query(self.request.GET, 'years_of_release')
        else:
            return Manga.objects.all()

    def get_context_data(self, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Каталог')
        context['category'] = Category.objects.all()
        context['values_filter'] = Manga.objects.values('years_of_release', 'transfer_status', 'rating')

        return dict(list(context.items()) + list(c_def.items()))
    
    @classmethod
    def sort_query(self, get_list, name_sort):
        query = Q()

        if 'cat' in get_list:
            query &= Q(cat__in=get_list.getlist('cat'))
        if 'status' in get_list:
            query &= Q(transfer_status__in=get_list.getlist('status'))
        if 'years_of_release' in get_list:
            print(get_list['years_of_release'])
            query &= Q(years_of_release__in=get_list.getlist('years_of_release'))
        
        if query:
            return Manga.objects.filter(query).order_by(name_sort)
        else:
            return Manga.objects.all().order_by(name_sort)