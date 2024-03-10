from django.db import models
from django.contrib.auth import get_user_model

from BlogApp.models import Manga


class Comment(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    sending_time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Отправитель')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Манга')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.sender.username} - {self.sending_time}'