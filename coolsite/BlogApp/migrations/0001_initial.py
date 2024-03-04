# Generated by Django 4.2.4 on 2024-03-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MangaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение манги')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
            ],
            options={
                'verbose_name': 'Изображение манги',
                'verbose_name_plural': 'Изображение манги',
                'ordering': ['time_create'],
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='3аголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Введение манги')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Рейтинг')),
                ('years_of_release', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год релиза')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('transfer_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статус перевода')),
                ('cat', models.ManyToManyField(to='BlogApp.category', verbose_name='Категории')),
                ('manga', models.ManyToManyField(to='BlogApp.mangaimage', verbose_name='Манга')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]