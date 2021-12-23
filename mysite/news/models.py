from django.db.models import Sum
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.models import ContentType

from imagekit.models.fields import ImageSpecField
from imagekit.processors import Adjust,ResizeToFill

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth import get_user_model
from userprofile.models import User

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='Удалён')[0]

#модель новостей
class News(models.Model):
    title = models.CharField("Загаловок", max_length = 115)
    small_text = RichTextUploadingField("Краткое описание",config_name='smallText', max_length=200)
    text = RichTextUploadingField("Текст новости")
    votes = GenericRelation('LikeDislike', related_query_name='news')
    date_pub = models.DateTimeField("Дата публикации", auto_now=False, default = timezone.now)
    image = models.ImageField("Изображение на обложку", default="")
    image_small = ImageSpecField([Adjust(contrast=1, sharpness=1),ResizeToFill(420, 240)], source='image',format='JPEG', options={'quality': 90})
    header_image = models.ImageField("Изображение сверху главной страницы", default="", blank=True)
    header_image_small = ImageSpecField([Adjust(contrast=1, sharpness=1),ResizeToFill(1600, 900)], source='image',format='JPEG', options={'quality': 90})
    author = models.ForeignKey(User, blank=True, on_delete=models.SET(get_sentinel_user), verbose_name = "Автор")

    message_count = models.IntegerField("Колличество сообщений", default=0)

    in_header = models.BooleanField("Разместить сверху главной страницы?" ,default=False)

    

    def counter(self, *args, **kwargs):
        self.message_count = self.newscomments_set.all().count()+1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_pub']

#модель коментариев
class NewsComments(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name = 'Новость')
    votes = GenericRelation('LikeDislike', related_query_name='news')
    text = RichTextUploadingField("Сообщение", config_name='comments', max_length=240)
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), verbose_name = "Автор")
    date_pub = models.DateTimeField("Дата публикации", auto_now=False, default = timezone.now)
    
    def save(self, *args, **kwargs):
        self.news.counter()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
    class Meta:
        verbose_name  = "Коментарий"
        verbose_name_plural = "Коментарии"

#универсальные модель для лайков и дизлайков (кмоентариев и новостей)
class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
 
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
 
    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )
 
    vote = models.SmallIntegerField(verbose_name=_("Голос"), choices=VOTES)
    user = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE)
 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_("К чему относится"))
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = LikeDislikeManager()

    class Meta:
        verbose_name = 'Лайк или Дизлайк'
        verbose_name_plural = 'Лайки-Дизлайки'




 




