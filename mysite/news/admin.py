from django.contrib import admin
from django.core.mail import send_mail 
from mysite.settings import DEFAULT_FROM_EMAIL
from news.models import LikeDislike, News, NewsComments
from userprofile.models import User

class NewsAdmin(admin.ModelAdmin):
    model = News
    fieldsets = (("Данные для входа", {'fields': ('author', 'title', 'image', 'header_image', 'in_header', 'small_text', 'text', 'date_pub')}),)
    list_display = ("title", "author", "in_header", "date_pub", "image", 'header_image')
    list_filter = ("in_header", "date_pub")
    search_fields = ("title", "author__username")

    actions = ("set_news_in_header_true", "set_news_in_header_false", "send_news")

    def send_news(self, request, queryset):
        users = User.objects.filter(get_news=True)
        i = 0
        for news in queryset.all():
            message =  news.text
            for user in users:
                i += 1
                send_mail('CyberPlace', '', DEFAULT_FROM_EMAIL, [user.email], fail_silently=False, html_message=message)
        self.message_user(request, 'Успешно. Новости были отправлены  ({})  пользователям'.format(i))
    send_news.short_description = "Отправить выбранные новости пользователям"

    def set_news_in_header_true(self, request, queryset):
        news = queryset.update(in_header=True)
        self.message_user(request, 'Успешно. Новости размещены сверху главной страницы. В количестве ({}) штк.'.format(news))
    def set_news_in_header_false(self, request, queryset):
        news = queryset.update(in_header=False)
        self.message_user(request, 'Успешно. Новости больше не сверху главной страницы. В количестве ({}) штк.'.format(news))
    set_news_in_header_true.short_description = "Поместить новость сверху главной страницы"
    set_news_in_header_false.short_description = "Убрать новость сверху главной страницы"

class LikeDislikeAdmin(admin.ModelAdmin):
    model = LikeDislike
    fieldsets = (("", {'fields': ("user", "vote", "content_type")}),)
    list_display = ("user", "vote", "content_type")
    list_filter = ("content_type", "vote")
    search_fields = ("user__username",)

class NewsCommentsAdmin(admin.ModelAdmin):
    model = NewsComments
    list_display = ("news", "text", "author", "date_pub")
    search_fields = ("text", "author")
    list_filter = ("news", "author", "date_pub")

admin.site.register(News, NewsAdmin)
admin.site.register(NewsComments, NewsCommentsAdmin)
admin.site.register(LikeDislike, LikeDislikeAdmin)
