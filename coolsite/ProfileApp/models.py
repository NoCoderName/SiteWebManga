from django.db import models
from django.contrib.auth.models import User

from BlogApp.models import Manga


class Profile(models.Model):
    photo = models.ImageField(upload_to='photo_user/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото пользователя')
    read = models.ManyToManyField(Manga, blank=True, verbose_name='Читают')
    read_it = models.ManyToManyField(Manga, blank=True, related_name='read_ it+', verbose_name='Прочитано')
    favorites = models.ManyToManyField(Manga, blank=True, related_name='favorites+', verbose_name='Избранное')
    abandoned = models.ManyToManyField(Manga, blank=True, related_name='abandoned+', verbose_name='Брошено')
    friends = models.ManyToManyField(User, blank=True, related_name='friends+', verbose_name='Друзья')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ['user',]