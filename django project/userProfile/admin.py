from django.contrib import admin
from django.core.mail import send_mail
from mysite.settings import DEFAULT_FROM_EMAIL
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.admin import UserAdmin
from userProfile.models import FriendRequest, FriendRequest, User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        ("Данные для входа", {'fields': ('username', 'password')}),

        (('Персональная информация'), {'fields': ('first_name', 'last_name','patronymic', 'email', 'image', 'phone','dateBirth', 'addres', 'gender', 'friends', 'skype', 'get_news')}),
        (('Права'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions'),}),
        (('Настройки адреса'), {'fields': ('slug',),}),
        # (('Настройки приватности'), {'fields': ('showRealName','showUsername')}),
        (('Дата и время'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1', 'password2'),
        }),
    )

    list_display = ("username", "email", "first_name", "last_name", "patronymic", "phone" , "dateBirth" , "addres", "gender", 'skype', "is_active", "is_staff", "is_superuser","slug", 'image')
    
    list_filter = ("is_active", "is_staff", "is_superuser", "dateBirth", "gender", "groups", "user_permissions",  "last_login", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name", "patronymic", "phone", "skype", "addres")

class FriendRequestAdmin(admin.ModelAdmin):
    model = FriendRequest
    list_display = ("to_user", "from_user")
    search_fields = ("to_user__username", "from_user__username")






admin.site.register(User, CustomUserAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)

