from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Модель для рассылки писем
class EmailMessage(models.Model):
    title = models.CharField("Загаловок", max_length = 100)
    message = RichTextUploadingField("Сообщение", config_name='email')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Email сообщение'
        verbose_name_plural = 'Email сообщения'