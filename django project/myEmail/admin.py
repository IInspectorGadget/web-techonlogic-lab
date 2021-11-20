from django.contrib import admin
from django.core.mail import send_mail
from .models import *
from mysite.settings import DEFAULT_FROM_EMAIL
from userProfile.models import User
# Register your models here.
class EmailMessageAdmin(admin.ModelAdmin):
    model = EmailMessage
    list_display = ("title", "message")
    search_fields = ("title", )

    actions = ("send_news", 'send_news_all')

    def send_news(self, request, queryset):
        users = User.objects.filter(get_news=True)
        i = 0
        for message in queryset.all():
            for user in users:
                i += 1
                send_mail(message.title, '', DEFAULT_FROM_EMAIL, [user.email], fail_silently=False, html_message=message.message)
        self.message_user(request, 'Успешно. Новости были отправлены  ({})  пользователям'.format(i))
    def send_news_all(self, request, queryset):
        users = User.objects.all()
        i = 0
        for message in queryset.all():
            for user in users:
                i += 1
                send_mail(message.title, '', DEFAULT_FROM_EMAIL, [user.email], fail_silently=False, html_message=message.message)
        self.message_user(request, 'Успешно. Новости были отправлены  ({})  пользователям'.format(i))

    send_news.short_description = "Отправить выбранные новости пользователям"
    send_news_all.short_description = "Отправить выбранные новости всем пользователям"
    
admin.site.register(EmailMessage, EmailMessageAdmin)
