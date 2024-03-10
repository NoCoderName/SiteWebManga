from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Manga(models.Model):
    title = models.CharField(max_length=255, verbose_name='3аголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Введение манги')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ManyToManyField('Category', verbose_name='Категории')
    manga = models.ManyToManyField('MangaImage', verbose_name='Манга')
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, verbose_name='Рейтинг')
    years_of_release = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год релиза')
    author = models.CharField(max_length=255, null=True, blank=True, verbose_name='Автор')
    transfer_status = models.CharField(max_length=255, null=True, blank=True, verbose_name='Статус перевода')

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


class Comment(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    sending_time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Отправитель')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Манга')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.sender.username} - {self.sending_time}'