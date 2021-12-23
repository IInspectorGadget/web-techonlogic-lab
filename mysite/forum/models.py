from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from userprofile.models import User
from django.utils import timezone

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='Удалён')[0]

class ForumTitle(models.Model):
    name = models.CharField("Название", max_length = 50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class ForumTop(models.Model):
    forumTitle = models.ForeignKey(ForumTitle, on_delete=models.CASCADE, verbose_name="Раздел")
    name = models.CharField("Название", max_length = 50)
    post_count = models.IntegerField("Колличество подтем", default=0)
    image = models.ImageField('Изоображение', default='')
    def __str__(self):
        return self.name

    def counter(self, *args, **kwargs):
        self.post_count = self.forummiddle_set.all().count() + 1
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'

class ForumMiddle(models.Model):
    forumTop = models.ForeignKey(ForumTop, on_delete=models.CASCADE, verbose_name="Тема")
    name = models.CharField("Название", max_length = 50)
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), verbose_name="Создатель", null=True)
    date_create = models.DateTimeField("Дата создания", default = timezone.now)
    post_count = models.IntegerField("Колличество сообщений", default=0)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.forumTop.counter()
        super().save(*args, **kwargs)

    def counter(self, *args, **kwargs):
        self.post_count = self.forummessage_set.all().count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подтему'
        verbose_name_plural = 'Подтемы'

class ForumMessage(models.Model):
    forumMiddle = models.ForeignKey(ForumMiddle, on_delete=models.CASCADE, verbose_name="Подтема")
    message = RichTextUploadingField("Сообщение" ,config_name='forum_message', max_length=1100)
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), verbose_name="Автор")
    date_pub = models.DateTimeField("Дата создания", default = timezone.now)
    
    def __str__(self):
        message = self.message.replace("p>","").replace("h1>","").replace("em>","").replace("</","").replace("<","")
        if(len(message) > 40):
            return message[:40] + "..."
        return message

    def save(self, *args, **kwargs):
        self.forumMiddle.counter()
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения форума'
