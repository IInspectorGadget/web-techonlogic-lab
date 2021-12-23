from django.contrib import admin
from forum.models import ForumMessage, ForumMiddle, ForumTitle, ForumTop

class ForumMessageAdmin(admin.ModelAdmin):
    model = ForumMessage
    list_display = ("forumMiddle", "__str__", "user", "date_pub")
    list_filter = ("forumMiddle", "date_pub")
    search_fields = ("user__username", "message")
class ForumMiddleAdmin(admin.ModelAdmin):
    model = ForumMiddle
    list_display = ("forumTop", "name", "user", "date_create", "post_count")
    list_filter = ("forumTop", "date_create")
    search_fields = ("name","user__username")

class ForumTopAdmin(admin.ModelAdmin):
    model = ForumTop
    list_display = ("forumTitle", "name", "post_count", "image")
    list_filter = ("forumTitle", )
    search_fields = ("name",)

class ForumTitleAdmin(admin.ModelAdmin):
    model = ForumTitle
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(ForumMessage, ForumMessageAdmin)
admin.site.register(ForumMiddle, ForumMiddleAdmin)
admin.site.register(ForumTop, ForumTopAdmin)
admin.site.register(ForumTitle, ForumTitleAdmin)