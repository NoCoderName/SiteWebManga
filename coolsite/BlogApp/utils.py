from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


menu = [
    {'title': 'Manga.ka', 'url_name': 'home'},
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'Поиск', 'url_name': 'about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context