from django import template
from BlogApp.models import *


register = template.Library()

@register.simple_tag(name='cats')
def get_categories():
    categories = Category.objects.all()
    cat_list = list()
    
    for category in categories:
        if category.manga_set.exists():
            cat_list.append(category)
    
    return cat_list