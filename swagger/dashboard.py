"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'mysite.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
            _('Коммуникация'),
            collapsible=False,
            column=1,
            css_classes=('collapse closed',),
            models=('userprofile.models.Telegram','userprofile.models.User','django.contrib.*','userprofile.models.Chat', 'userprofile.models.Message', 'userprofile.models.FriendRequest', 'myEmail.models.EmailMessage')
        ))

        self.children.append(modules.ModelList(
            _('Форум'),
            collapsible=False,
            column=1,
            css_classes=('collapse closed',),
            models=('forum.models.ForumMessage','forum.models.ForumMiddle','forum.models.ForumTop', 'forum.models.ForumTitle')
        ))
        self.children.append(modules.ModelList(
            _('Новости'),
            collapsible=False,
            column=1,
            css_classes=('collapse closed',),
            models=('news.models.News', 'news.models.NewsComments', 'news.models.LikeDislike')
        ))

        self.children.append(modules.RecentActions(
            _('Ваши последние действия'),
            limit=10,
            collapsible=False,
            column=3,
        ))