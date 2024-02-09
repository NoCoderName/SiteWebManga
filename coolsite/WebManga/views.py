import sys
from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, get_user_model

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .utils import *
from .forms import *


class MangaHome(DataMixin, ListView):
    model = Manga
    template_name = 'WebManga/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')

        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Manga.objects.filter(is_published=True)
    
def category(request):
    return HttpResponse('категории')


class About(DataMixin, ListView):
    model = Manga
    template_name = 'WebManga/about.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')

        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse('Свя3ь с ра3работчиком')


class Showpost(DataMixin, DetailView):
    model = Manga
    template_name = 'WebManga/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'WebManga/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'WebManga/login.html'

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')
    

def logout_user(request):
    logout(request)

    return redirect('login')


class MessageUser(DataMixin, CreateView):
    form_class = MessageForm
    template_name = 'WebManga/chat.html'

    def get_context_data(self, *, object_name= None, **kwargs):
        context = super().get_user_context(**kwargs)
        c_def = self.get_user_context(title='Чат')

        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.message = form.cleaned_data['message']
        
        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse('chat')
    

# class AddManga(DataMixin, CreateView):
#     model = User
#     context_object_name = 'add'
#     slug_url_kwarg = 'post_slug'
#     template_name = 'WebManga/index.html'
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         manga = Manga.objects.get(self.slug_url_kwarg)
#         form.instance.read = manga
#         return super().form_valid(form)