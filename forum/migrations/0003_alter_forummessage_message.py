# Generated by Django 3.2 on 2021-11-16 19:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forummessage_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forummessage',
            name='message',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1100, verbose_name='Сообщение'),
        ),
    ]
