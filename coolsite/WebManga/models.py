from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Manga(models.Model):
    title = models.CharField(max_length=255, verbose_name='3аголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Введение манги')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    manga = models.ManyToManyField('MangaImage', verbose_name='Манга')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'
        ordering = ['-time_create', 'title']
        

class MangaImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение манги')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Изображение манги'
        verbose_name_plural = 'Изображение манги'
        ordering = ['time_create']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
    

class User(AbstractUser):
    photo = models.ImageField(upload_to='photo_user/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото пользователя')
    read = models.ForeignKey(Manga, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Читают')
    
    # def __str__(self):
    #     return self.user.username
    

class Message(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    sending_time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
    sender = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Отправитель')

    def __str__(self):
        return f'{self.sender.username} - {self.sending_time}'