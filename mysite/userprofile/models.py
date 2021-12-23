from django.db import models
from userprofile import validators
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.utils import dateformat, timezone
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

from django.contrib.auth.models import AbstractUser
from imagekit.models.fields import ImageSpecField

class User(AbstractUser):
    db_table = 'user'
    username = models.CharField('имя пользователя', max_length=150,unique=True, help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[validators.user_slug],
        error_messages={'unique': _("Пользователь с таким именем уже существует."),},
    )
    email = models.EmailField(_('Адрес электронной почты'), blank=False)

    get_news = models.BooleanField('Получать новости', default= False)
    image = models.ImageField('фото',upload_to='UserAvatars', default = 'UserAvatars/default.png')
    image_small = ImageSpecField([Adjust(contrast=1, sharpness=1),ResizeToFill(260, 256)], source='image',format='JPEG', options={'quality': 90})

    slug = models.SlugField('слыка на профиль', default = '')
    patronymic = models.CharField('Отчество', max_length=30, blank=True)
    
    dateBirth = models.DateField('дата рождения',blank=True, null=True)
    phone_validator = RegexValidator('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message="Введите правильный номер.")
    
    phone = models.CharField('телефон',validators=[phone_validator],max_length = 30, blank=True, default='')

    skype = models.CharField('скайп', max_length = 30, blank=True, default="")
    addres = models.TextField('адресс', max_length = 200, blank=True, default="")
    # organization = models.CharField('название организации', max_length = 100, blank=True, default="")
    

    friends = models.ManyToManyField("User", blank=True, verbose_name="Друзья", help_text = 'Удерживайте "Control", или "Command" на Mac, чтобы выбрать больше одного пользователя /// ')
    # showUsername = models.BooleanField('Показывать Имя', default= False)
    # showRealName = models.BooleanField('Показывать Фамилию', default= False)

    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE, verbose_name = "Получатель")
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE, verbose_name = "Отправитель")

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)

    class Meta:
        verbose_name = 'Запрос в друзья'
        verbose_name_plural = 'Запросы в друзья'

class Telegram(models.Model):
    user = models.ForeignKey(User, related_name='teluser', on_delete=models.CASCADE, verbose_name = "Пользователь")
    telegram_id = models.IntegerField("Телеграм id", default=0)
