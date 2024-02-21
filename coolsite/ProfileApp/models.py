from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model

from BlogApp.models import Manga


class ProfileUser(AbstractUser):
    photo = models.ImageField(upload_to='photo_user/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото пользователя')
    read = models.ManyToManyField(Manga, blank=True, related_name='read+', verbose_name='Читают')
    read_it = models.ManyToManyField(Manga, blank=True, related_name='read_ it+', verbose_name='Прочитано')
    favorites = models.ManyToManyField(Manga, blank=True, related_name='favorites+', verbose_name='Избранное')
    abandoned = models.ManyToManyField(Manga, blank=True, related_name='abandoned+', verbose_name='Брошено')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'prof_slug': self.slug})
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ['id',]