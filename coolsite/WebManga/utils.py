from .models import *

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Связь с разработчиком', 'url_name': 'contact'},
    # {'title': 'Чат', 'url_name': 'chat'},
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