# Generated by Django 3.2 on 2021-12-23 14:44

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], verbose_name='Голос')),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Лайк или Дизлайк',
                'verbose_name_plural': 'Лайки-Дизлайки',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=115, verbose_name='Загаловок')),
                ('small_text', ckeditor_uploader.fields.RichTextUploadingField(max_length=200, verbose_name='Краткое описание')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст новости')),
                ('date_pub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('image', models.ImageField(default='', upload_to='', verbose_name='Изображение на обложку')),
                ('header_image', models.ImageField(blank=True, default='', upload_to='', verbose_name='Изображение сверху главной страницы')),
                ('message_count', models.IntegerField(default=0, verbose_name='Колличество сообщений')),
                ('in_header', models.BooleanField(default=False, verbose_name='Разместить сверху главной страницы?')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date_pub'],
            },
        ),
        migrations.CreateModel(
            name='NewsComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(max_length=240, verbose_name='Сообщение')),
                ('date_pub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
