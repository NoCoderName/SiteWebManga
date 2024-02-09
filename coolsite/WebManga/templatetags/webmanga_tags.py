from django import template
from WebManga.models import *


register = template.Library()

@register.simple_tag(name='cats')
def get_categories():
    categories = Category.objects.all()
    cat_list = list()
    
    for category in categories:
        if category.manga_set.exists():
            cat_list.append(category)
    
    return cat_list

@register.simple_tag(name='message')
def get_message():
    message = Message.objects.all()

    return message

@register.inclusion_tag('WebManga/label_box.html')
def label_box():
    pass

# @register.simple_tag(name='UserProfile')
# def get_check_value(request):
#     checkbox = request.POST.get('add_post')
#     if checkbox:
#         manga_pk = request.POST.get('manga_pk')
#         user_name = ProfileUser.objects.get(user__username=request.POST.get('user_name'))
#         return user_name.read.add(manga_pk).save()


# def add_recording(user_name):
#     return ProfileUser.objects.get(user__username=user_name)


# def get_check_value(request):
#     checkbox = request.POST.get('add_post')
#     if checkbox:
#         manga_pk = request.POST.get('manga_pk')
#         user_name = ProfileUser.objects.get(user__username=request.POST.get('user_name'))
#         return user_name.read.add(manga_pk)

# def add_recording(manga_pk, user_name):
#     manga = Manga.objects.get(pk=manga_pk)
#     user = ProfileUser.objects.get(user__username=user_name)
    
#     return user.read.add(manga)